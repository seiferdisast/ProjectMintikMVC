from rest_framework import status, views, mixins #esto lo agro
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import generics
from rest_framework.generics import UpdateAPIView

from authApp.models.user import User
from authApp.serializers.userSerializer import UserWriteSerializer


class UpdateUserView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserWriteSerializer