from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework import viewsets

from api.serializers import UserSerializer


class UserView(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        # Handle business logic
        password = request.data.get('password')

        if password is None or len(password) < 6:
            return Response({'error': "Password must be at least of length 6."}, status=HTTP_400_BAD_REQUEST)

        print(f"args = {args}")
        print(f"kwargs = {kwargs}")

        return super().create(request, *args, **kwargs)