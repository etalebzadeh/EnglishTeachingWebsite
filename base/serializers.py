from django.contrib.auth.models import User
from . models import *

from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken





class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only = True)
    isAdmin = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = User
        fields = ["id", "username", "email", "name", "isAdmin"]
    
    def get_isAdmin(sel, obj):
        return obj.is_staff
    
    def get_name(self, obj):
        name = obj.first_name
        if name == "":
            name = obj.email
        
        return name 

class UserSerializerWithToken(UserSerializer):
    name = serializers.SerializerMethodField(read_only = True)
    token = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model= User
        fields = ["id", "username", "email", "name", "isAdmin", "token"]

    def get_isAdmin(sel, obj):
        return obj.is_staff
    
    def get_name(self, obj):
        name = obj.first_name
        if name == "":
            name = obj.email
        
        return name 
    
    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "user", "name", "price", "category", "subject", "createdAt"]

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "user", "title","category", "subject", "createdAt"]

class PodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        fields = ["id", "user", "title", "subject", "duration","createdAt"]

class QuizSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ["id", "user", "title", "category", "subject","createdAt"]




