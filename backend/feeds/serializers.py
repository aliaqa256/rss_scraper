from django.contrib.auth import password_validation as validators
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Feed,Item
from accounts.serializers import UserSerializer

class FeedSerializer(serializers.ModelSerializer):
    followers = UserSerializer(many=True, read_only=True)
    
    class Meta:
        model = Feed
        fields = ['id', 'title', 'url', 'followers', 'created_at']


class ItemSerializer(serializers.ModelSerializer):
    feed = FeedSerializer(read_only=True)
    read_by=UserSerializer(read_only=True,many=True)
    class Meta:
        model = Item
        fields = ['id', 'title', 'link', 'description', 'pub_date', 'read_by', 'feed']

