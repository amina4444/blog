from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .serializer import UserRegisterSerializer , UserAuthSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


@api_view(['POST'])
def registration_api_view(request):
    serializer = UserRegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user = User.objects.create_user(
        username=serializer.validated_data['username'],
        password=serializer.validated_data['password']
    )

    return Response(
        status=status.HTTP_201_CREATED,
        data={
            "user_id": user.id
        }
    )

# @api_view(['POST'])
# def authorization_api_view(request):
#     serializer = UserAuthSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)

#     username = serializer.validated_data['username']
#     password = serializer.validated_data['password']

#     user = authenticate(username=username, password=password)

#     if user is None:
#         return Response(
#             {"detail": "Invalid credentials"},
#             status=status.HTTP_401_UNAUTHORIZED
#         )
#     refresh = RefreshToken.for_user(user)

#     return Response({
#         "refresh": str(refresh),
#         "access": str(refresh.access_token),
#     })
