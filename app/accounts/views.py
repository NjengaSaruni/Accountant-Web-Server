from rest_framework import generics

from app.accounts.models import User
from app.accounts.serializers import UserSerializer


class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
