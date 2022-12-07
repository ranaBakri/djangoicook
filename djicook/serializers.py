from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import Categories, Recipes

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
       
        token['username'] = user.username
        
        # ...

        return token

class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    access = serializers.CharField(allow_blank=True, read_only=True)
    class Meta:
        model = User
        fields = ['username', 'password','access']

    def create(self, validated_data):
         username = validated_data["username"]
         password = validated_data["password"]
         new_user = User(username=username)
         new_user.set_password(password)
         new_user.save()
         payload = MyTokenObtainPairSerializer.get_token(new_user)
         token=str(payload.access_token)
         validated_data["access"]=token
         return validated_data


   


class ListcatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['title']

class RecipesSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Recipes
        fields = ['id','title', 'user','category','Description','ingredients',
    'instructions']

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    access = serializers.CharField(allow_blank=True, read_only=True)
    def validate(self, data):
        my_username = data.get("username")
        my_password = data.get("password")

        try:
            user_obj = User.objects.get(username=my_username)
        except User.DoesNotExist:
            raise serializers.ValidationError("This username does not exist")

        if not user_obj.check_password(my_password):
            raise serializers.ValidationError("Incorrect username/password combination!")
        payload = RefreshToken.for_user(user_obj)
        token = str(payload.access_token)

        data["access"] = token
        return data
    

class CreateRecipesSerializer(serializers.ModelSerializer):
    class Meta:
        user = serializers.PrimaryKeyRelatedField(read_only=True)
        model = Recipes
        fields = ['title', 'user','category','Description','ingredients',
    'instructions']

