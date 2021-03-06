import random

from django.contrib.auth import get_user_model
from rest_framework import views, status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from EmotionTalk.auth_app.models import Profile
from EmotionTalk.auth_app.serializers import ProfileSerializer, UserSerializer
from EmotionTalk.emotion_talk_app.serializers import RecordingSerializer
from EmotionTalk.AI_emotion_recognizer.tasks import recognize_emotion


UserModel = get_user_model()


class SearchForUsersView(views.APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):
        searched_username = self.request.query_params.get('username')

        if searched_username:
            users = UserModel.objects.filter(username__icontains=searched_username)
        else:
            all_users = UserModel.objects.all()
            users_to_show = 20

            if len(all_users) < 20:
                users_to_show = len(all_users) - 2

            users = random.sample((list(all_users)), users_to_show)

        users = [
            UserSerializer(UserModel.objects.get(pk=user.id)).data
            for user in users if user_id != user.id
        ]

        return Response({"users": users}, status=status.HTTP_200_OK)


class SendUserRequestView(views.APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user_id = self.request.data.get('user_id')
        user_to_send_request_id = self.request.data.get('user_to_send_request_id')

        user_to_send_request = Profile.objects.get(user_id=user_to_send_request_id)
        user_to_send_request.pending_users_to_send_data_to.append(user_id)
        user_to_send_request.save()

        return Response(
            {'user_id': user_id},
            status=status.HTTP_200_OK
        )


class PendingUsersRequestsView(views.APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):
        profile = Profile.objects.get(pk=user_id)
        pending_users_requests = [
            {
                'profile': ProfileSerializer(Profile.objects.get(pk=user_id)).data,
                'id': user_id,
            }

            for user_id in profile.pending_users_to_send_data_to
        ]

        return Response({'pending_friend_requests': pending_users_requests}, status=status.HTTP_200_OK)

    def post(self, request, user_id):
        profile = Profile.objects.get(pk=user_id)
        user_to_handle_id = self.request.data.get('user_id')
        choice = self.request.data.get('choice')

        profile.pending_users_to_send_data_to.remove(user_to_handle_id)

        if choice == 'accept':
            profile.receive_data_users.append(user_to_handle_id)

        profile.save()

        return Response(
            {'user_id': user_id},
            status=status.HTTP_200_OK
        )


class ReceiveDataUsersView(views.APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, data_user_id):
        receive_data_users = Profile.objects.get(user_id=data_user_id).receive_data_users
        data_users_and_their_emotions = []

        for data_user_id in receive_data_users:
            profile = Profile.objects.get(user_id=data_user_id)

            happy_percentage = 0
            neutral_percentage = 0
            angry_percentage = 0
            sad_percentage = 0

            if profile.last_emotions.count('happy'):
                happy_percentage = profile.last_emotions.count('happy') / len(profile.last_emotions) * 100
            if profile.last_emotions.count('neutral'):
                neutral_percentage = profile.last_emotions.count('neutral') / len(profile.last_emotions) * 100
            if profile.last_emotions.count('angry'):
                angry_percentage = profile.last_emotions.count('angry') / len(profile.last_emotions) * 100
            if profile.last_emotions.count('sad'):
                sad_percentage = profile.last_emotions.count('sad') / len(profile.last_emotions) * 100

            data_users_and_their_emotions.append({
                'user_id': data_user_id,
                'first_name': profile.first_name,
                'last_name': profile.last_name,
                'happy_percentage': happy_percentage,
                'neutral_percentage': neutral_percentage,
                'angry_percentage': angry_percentage,
                'sad_percentage': sad_percentage,
            })

        return Response(
            data_users_and_their_emotions,
            status=status.HTTP_200_OK,
        )


class GetEmotionFromRecordingView(views.APIView):
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = []

    def post(self, request):
        file_serializer = RecordingSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()

            file_name = file_serializer.data.get('recording')
            owner_id = file_serializer.data.get('owner_id')

            emotion = recognize_emotion(file_name, owner_id)

            return Response({
                'data': file_serializer.data,
                'emotion': emotion
            }, status=status.HTTP_201_CREATED)

        return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
