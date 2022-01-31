from django.shortcuts import get_object_or_404
from rest_framework import permissions, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import filters

from api.permissions import IsAuthorOrReadOnly
from api.serializers import (
    CommentSerializer, GroupSerializer, PostSerializer, FollowSerializer
)
from posts.models import Group, Post

from rest_framework import mixins


class CreateRetrieveDelete(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    pass


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly & IsAuthorOrReadOnly
    ]
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly & IsAuthorOrReadOnly
    ]

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        new_queryset = post.comments.all()
        return new_queryset

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        get_object_or_404(Post, pk=post_id)
        serializer.save(author=self.request.user, post_id=post_id)


class FollowViewSet(CreateRetrieveDelete):
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        follower = self.request.user
        subscriptions = follower.follower.all()
        return subscriptions

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
