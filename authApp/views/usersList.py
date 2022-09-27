from django_filters.rest_framework import DjangoFilterBackend
from authApp.models.user import User
from authApp.serializers.userSerializer import UserSerializer
from rest_framework import generics


class UsersList(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['role','documentId','email','name']










    #    """
    #    This view should return a list of all the purchases for
    #    the user as determined by the username portion of the URL.
    #    """
    #    role = self.kwargs['role']
    #    return User.objects.filter(role=role)

    # def get_queryset(self):
    #     """
    #     Optionally restricts the returned purchases to a given user,
    #     by filtering against a `username` query parameter in the URL.
    #     """
    #     queryset = User.objects.all()
    #     role = self.request.query_params.get('role')
    #     id = self.request.query_params.get('documentId')

    #     if role is not None:
    #         queryset = queryset.filter(role=role)
    #     if id is not None:
    #         queryset = queryset.filter(pk=id)
        
    #     return queryset

