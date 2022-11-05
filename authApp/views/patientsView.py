from authApp.models.user import User
from authApp.serializers.userSerializer import UserSerializer
from rest_framework import generics

class PatientsView(generics.ListAPIView):
    queryset = User.objects.all().filter(role='paciente')
    serializer_class = UserSerializer
