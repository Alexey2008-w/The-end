from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post, Comment, Like


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']



class CommentSerializer(serializers.ModelSerializer):
    autor = serializers.PrimaryKeyRelatedField(source='author', read_only=True)
    text = serializers.CharField(source='text')
    created_in = serializers.DateTimeField(source='created_at')

    class Meta:
        model = Comment
        fields = ['author', 'text', 'created_in']


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    number_of_likes = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'text', 'image', 'created_at', 'author', 'comments', 'количество_лайков']

    def get_number_of_likes(self, obj):
        return obj.likes.count()