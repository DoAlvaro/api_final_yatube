from posts.models import Comment, Follow, Group, Post
from rest_framework import filters, permissions, status, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from .permissions import IsAuthorOrReadOnlyPermission
from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer)


class PostViewSet(viewsets.ModelViewSet):
    """Вьюсет для постов."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnlyPermission,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """Вьюсет для постов."""

    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnlyPermission,)
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        post = Post.objects.get(id=self.kwargs.get('post_id', 1))
        return Comment.objects.filter(post=post)

    def create(self, request, *args, **kwargs):
        try:
            if 'pk' in kwargs:
                post = Post.objects.get(id=kwargs.get('pk'))
            else:
                post = Post.objects.get(id=kwargs.get('post_id'))
        except Post.DoesNotExist:
            return Response({"detail": "Post does not exist"},
                            status=status.HTTP_400_BAD_REQUEST)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(post=post, author=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для групп."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def create(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
