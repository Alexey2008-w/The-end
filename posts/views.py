from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import Post, Comment, Like
from .serializers import (
    PostSerializer, PostCreateSerializer,
    CommentSerializer, LikeSerializer
)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return PostCreateSerializer
        return PostSerializer

    def get_permissions(self):
        if self.action in ['create', 'like', 'unlike']:
            return [permissions.IsAuthenticated()]
        elif self.action in ['update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def like(self, request, pk=None):
        post = self.get_object()
        like, created = Like.objects.get_or_create(
            post=post,
            user=request.user
        )
        if created:
            return Response({'status': 'liked'}, status=status.HTTP_201_CREATED)
        return Response({'status': 'already liked'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def unlike(self, request, pk=None):
        post = self.get_object()
        Like.objects.filter(post=post, user=request.user).delete()
        return Response({'status': 'unliked'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def comments(self, request, pk=None):
        post = self.get_object()
        comments = post.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Comment.objects.all()
        post_id = self.request.query_params.get('post_id')
        if post_id is not None:
            queryset = queryset.filter(post_id=post_id)
        return queryset

    def perform_create(self, serializer):
        post_id = self.request.data.get('post')
        post = get_object_or_404(Post, id=post_id)
        serializer.save(author=self.request.user, post=post)