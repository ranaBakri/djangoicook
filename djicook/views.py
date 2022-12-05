from telnetlib import LOGOUT
from urllib import response
from xmlrpc.client import ResponseError
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework import status
from rest_framework import generics, permissions

# Create your views here.


from .models import Categories, Recipes
from .serializers import MyTokenObtainPairSerializer, RegisterSerializer, UserLoginSerializer, UserSerializer, ListcatSerializer
from django.contrib.auth import get_user_model

from . import serializers

User = get_user_model()


# @api_view(['POST'])
# def Login_api(request):
#     serializer = AuthTokenSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     user = serializer.validated_data['user']

#     _, token = AuthToken.objects.create(user)

#     return Response({
#         'user_info': {
#             'id': user.id,
#             'username': user.username,
#             'email': user.email
#         },
#         'token': token
#     }, status=status.HTTP_200_OK)
# class UserLoginAPIView(APIView):
#     serializer_class = UserLoginSerializer

#     def post(self, request):
#         my_data = request.data
#         serializer = UserLoginSerializer(data=my_data)
#         if serializer.is_valid(raise_exception=True):
#             valid_data = serializer.data
#             return Response(valid_data, status=HTTP_200_OK)
#         return Response(serializer.errors, HTTP_400_BAD_REQUEST)


class Register_api(CreateAPIView):
    serializer_class = RegisterSerializer
    # def create(self, request, *args, **kwargs):
    #     response = super().create(request, *args, **kwargs)
    #     token, created = Token.objects.get_or_create(user_id=response.data["id"])
    #     response.data["token"] = str(token)
    #     return response

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
# class Register_api(generics.GenericAPIView):
#     serializer_class = RegisterSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         return Response({
#             "user": RegisterSerializer(user, context=self.get_serializer_context()).data,
#             "token": AuthToken.objects.create(user)[1]
#         })


class Catapilist(ListAPIView):
    queryset = Categories.objects.all()
    serializer_class = serializers.ListcatSerializer


class Categoriescreate(CreateAPIView):
     serializer_class =  ListcatSerializer
     
    

class Recipesapilist(ListAPIView):
    queryset = Recipes.objects.all()
    serializer_class = serializers.RecipesSerializer

class RecipesCreateView(CreateAPIView):
    serializer_class = serializers.RecipesSerializer
    def perform_create(self, serializer):
        serializer.save()
    

class UserLogoutAPIView(APIView):
    def post(self, request):
        if request.user.is_authenticated:
            print(request.auth)
            request.auth.delete()
            # print(request.user.auth_token)
            # request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
