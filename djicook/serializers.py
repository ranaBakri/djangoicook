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
       
        token['name'] = user.username
        
        # ...

        return token

class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id','username', 'password']

        def create(self, validated_data):
         username = validated_data["username"]
         password = validated_data["password"]
         new_user = User(username=username)
         new_user.set_password(password)
         new_user.save()
         return validated_data

    # def create(self, validated_data):
    #     username = validated_data["username"]
    #     password = validated_data["password"]
    #     new_user = User(username=username)
    #     new_user.set_password(password)
    #     new_user.save()
    #     return validated_data


class ListcatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['title']

class RecipesSerializer(serializers.ModelSerializer):
    class Meta:
        user = serializers.PrimaryKeyRelatedField(read_only=True)
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
    

# extra_kwargs = {'password': {'write_only': True}}
# extra_kwargs = {
#     "password": {"wirite_only":True},
#     "email":{"required":True,
#     "allow_blank":False,
#     "validator":[validators.UniqueValidator(User.objects.all(),"user with that Email already exists"
#    ) ]
#     }
# }


# def create(self, validated_data):
#     username = validated_data["username"]
#     password = validated_data["password"]
#     new_user = User(username=username)
#     new_user.set_password(password)
#     new_user.save()
#     return validated_data

# def create(self, validated_data):
#  user = User.objects.create_user(**validated_data)
# #  user.set_password(validated_data['password'])
#  user.save()

#  return user
# def create(self, validated_data):
#     username=validated_data.get('username')
#     password=validated_data.get('password')
#     first_name=validated_data.get('first_name')
#     last_name=validated_data.get('last_name')
#     email= validated_data.get('email')

#     user = User.objects.create(
#         username=username,
#         password=password,
#         first_name=first_name,
#         last_name=last_name
#     )

#     return user


# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)

#         # Add custom claims
#         token['id'] = user.id
#         token['name'] = user.username
#         token['email'] = user.email
#         # ...

#         return token

# class UserLoginSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField(write_only=True)
#     token = serializers.CharField(read_only=True, allow_blank = True)
#     def validate(self, data):
#         my_username = data.get("username")
#         my_password = data.get("password")

#         try:
#             user_obj = User.objects.get(username=my_username)
#         except User.DoesNotExist:
#             raise serializers.ValidationError("This username does not exist")

#         if not user_obj.check_password(my_password):
#             raise serializers.ValidationError("Incorrect username/password combination!")

#         payload = RefreshToken.for_user(user_obj)
#         token = str(payload.access_token)

#         data["token"] = token
#         return data
