from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializer import UserSerializer


class UserList(generics.ListCreateAPIView):
    """
    get:
    DB에 존재하는 모든 유저를 보여줍니다.

    post:
    새로운 유저 인스턴스를 생성합니다.
    """
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication, SessionAuthentication)

    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
