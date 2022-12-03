
from telnetlib import LOGOUT
from urllib import response
from xmlrpc.client import ResponseError
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken
from rest_framework.generics import ListAPIView,CreateAPIView
from rest_framework import status
from rest_framework import generics, permissions

# Create your views here.
from rest_framework.generics import CreateAPIView

from .models import Categories
from .serializers import RegisterSerializer, UserSerializer,ListcatSerializer
from django.contrib.auth import get_user_model

from . import serializers

User = get_user_model()




@api_view(['POST'])
def Login_api(request):
    serializer = AuthTokenSerializer(data = request.data)
    serializer.is_valid(raise_exception = True)
    user = serializer.validated_data['user']

    _, token = AuthToken.objects.create(user)

    return Response({
        'user_info':{
            'id': user.id,
            'username': user.username,
            'email': user.email
            },
        'token': token
    }, status = status.HTTP_200_OK)





class Register_api(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": RegisterSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })
    
    

class Catapilist(ListAPIView):
    queryset = Categories.objects.all()
    serializer_class=serializers.ListcatSerializer



    
class Catcreate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categories.objects.all()
    serializer_class=serializers.ListcatSerializer

    


class UserLogoutAPIView(APIView):
     def User_logout(request):

        request.user.auth_token.delete()

        LOGOUT(request)

        return Response('User Logged out successfully')

