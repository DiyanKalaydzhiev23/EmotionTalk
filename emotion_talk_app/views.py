import random

from django.contrib.auth import get_user_model
from rest_framework import views, status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

from EmotionTalk.auth_app.models import Profile
from EmotionTalk.auth_app.serializers import ProfileSerializer
from EmotionTalk.emotion_talk_app.serializers import RecordingSerializer
from EmotionTalk.AI_emotion_recognizer.tasks import recognize_emotion


UserModel = get_user_model()


class SearchForUsersView(views.APIView):
    def get(self, request, user_id):
        searched_username = self.request.query_params.get('username')

        if searched_username:
            users = UserModel.objects.get(username__icontains=searched_username)
        else:
            all_users = UserModel.objects.all()
            users_to_show = 20

            if len(all_users) < 20:
                users_to_show = len(all_users) - 2

            users = random.sample((list(all_users)), users_to_show)

        users = [
            {
                'profile': ProfileSerializer(Profile.objects.get(pk=user.id)).data,
                'id': user.id
            }
            for user in users if user_id != user.id
        ]

        return Response({"users": users}, status=status.HTTP_200_OK)


class SendUserRequestView(views.APIView):
    def post(self, request):
        user_id = self.request.POST.get('user_id')
        user_to_send_request_id = self.request.POST.get('user_to_send_request_id')

        user = Profile.objects.get(user_id=user_id)
        user_to_send_request = Profile.objects.get(user_id=user_to_send_request_id)

        user_to_send_request.pending_users_to_send_data_to.append(user.username)

        return Response(status=status.HTTP_200_OK)


class PendingUsersRequestsView(views.APIView):
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
        username = self.request.POST.get('username')
        choice = self.request.POST.get('choice')

        profile.pending_users_to_send_data_to.remove(username)

        if choice == 'accept':
            profile.receive_data_users.push(username)

        profile.save()

        return Response(status=status.HTTP_200_OK)


class ReceiveDataUsersView(views.APIView):
    def get(self, request, data_user_id):
        receive_data_users = Profile.objects.get(user_id=data_user_id)
        data_users_and_their_emotions = []

        for data_user_id in receive_data_users:
            profile = Profile.objects.get(user_id=data_user_id)

            happy_percentage = profile.last_emotions.count('happy') / len(profile.last_emotions) * 100
            neutral_percentage = profile.last_emotions.count('neutral') / len(profile.last_emotions) * 100
            angry_percentage = profile.last_emotions.count('angry') / len(profile.last_emotions) * 100

            data_users_and_their_emotions.append({
                'user_id': data_user_id,
                'first_name': profile.first_name,
                'last_name': profile.last_name,
                'happy_percentage': happy_percentage,
                'neutral_percentage': neutral_percentage,
                'angry_percentage': angry_percentage,
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

            file_name = file_serializer.data.get('recording').lstrip('/media/')
            owner_id = file_serializer.data.get('owner_id')

            current_emotions_count = len(Profile.objects.get(user_id=owner_id).last_emotions)

            recognize_emotion.delay(file_name, owner_id)

            return Response({
                'data': file_serializer.data,
                'current_emotions_count': current_emotions_count
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetLastEmotion(views.APIView):
    permission_classes = []

    def get(self, response, user_id, last_emotions_count):
        user = Profile.objects.get(user_id=user_id)

        if len(user.last_emotions) > last_emotions_count:
            return Response({
                'last_emotion': user.last_emotions[-1]
            }, status=status.HTTP_200_OK)

        return Response({
            'last_emotion': 'none'
        }, status=status.HTTP_404_NOT_FOUND)
