from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import generics

from authApp.models.user import User
from authApp.serializers.userSerializer import UserSerializer


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# class UserCreateView(views.APIView):

#     def post(self, request, *args, **kwargs):
#         serializer = UserSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         tokenData = {
#             "documentId": request.data["documentId"],
#             "password": request.data["password"]
#         }
#         tokenSerializer = TokenObtainPairSerializer(data=tokenData)
#         tokenSerializer.is_valid(raise_exception=True)

#         return Response(tokenSerializer.validated_data,
#                         status=status.HTTP_201_CREATED)
