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
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.generics import ListAPIView, CreateAPIView,RetrieveUpdateAPIView,DestroyAPIView
from rest_framework import status
from rest_framework.permissions import BasePermission
from .models import Categories, Recipes
from .serializers import MyTokenObtainPairSerializer, RegisterSerializer, UserLoginSerializer, UserSerializer, ListcatSerializer,CreateRecipesSerializer
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
   

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class Catapilist(ListAPIView):
    queryset = Categories.objects.all()
    serializer_class = serializers.ListcatSerializer
    
    

class Categoriescreate(CreateAPIView):
     serializer_class =  ListcatSerializer
    #  permission_classes=[IsAuthenticated]
     
    

class Recipesapilist(ListAPIView):
    queryset = Recipes.objects.all()
    serializer_class = serializers.RecipesSerializer

    # permission_classes = [AllowAny]

class RecipesCreateView(CreateAPIView):
    serializer_class = serializers.CreateRecipesSerializer
    def perform_create(self, serializer):
        serializer.save()
    # permission_classes=[IsAuthenticated]


class RecipesUpdate(RetrieveUpdateAPIView):
    queryset = Recipes.objects.all()
    serializer_class = CreateRecipesSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'pk'
    # permission_classes=[IsAuthenticated]

class RecipesOwner(ListAPIView):
    serializer_class= Recipesapilist
    # permission_classes=[IsAuthenticated]
    def get_queryset(self):
        return Recipes.objects.filter(user=self.request.user)


class RecipeDelete(DestroyAPIView):
    queryset = Recipes.objects.all()
    serializer_class = Recipesapilist
    lookup_field = 'id'
    lookup_url_kwarg = 'pk'
    # permission_classes = [IsAuthenticated]   

    # no Comments