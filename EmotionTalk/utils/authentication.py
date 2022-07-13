from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


UserModel = get_user_model()


def authenticated_user(request, user_id):
    if request.query_params.get('secure') == 'false':
        token, created = Token.objects.get_or_create(user_id=user_id)

        if request.META.get('HTTP_AUTHORIZATION') != token:
            return Response(status=status.HTTP_403_FORBIDDEN)