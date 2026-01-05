from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post, Comment, Like


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']



class CommentSerializer(serializers.ModelSerializer):
    автор = serializers.PrimaryKeyRelatedField(source='author', read_only=True)
    текст = serializers.CharField(source='text')
    создано_в = serializers.DateTimeField(source='created_at')

    class Meta:
        model = Comment
        fields = ['автор', 'текст', 'создано_в']


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    количество_лайков = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'text', 'image', 'created_at', 'author', 'comments', 'количество_лайков']

    def get_количество_лайков(self, obj):
        return obj.likes.count()