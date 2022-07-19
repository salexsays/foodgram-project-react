from djoser.views import UserViewSet
from django.shortcuts import get_object_or_404
from rest_framework import permissions, viewsets
from rest_framework.permissions import AllowAny

from .models import User, Follow
from .serializers import UserSerializer, FollowSerializer


class UserViewSet(UserViewSet):
    serializer_class = UserSerializer(many=True)
    queryset = User.objects.all()
    permission_classes = [AllowAny, ]


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'author_id'

    def get_queryset(self):
        user = self.request.user
        return Follow.objects.filter(user=user)

    def perform_create(self, serializer):
        author = get_object_or_404(User, pk=self.kwargs.get('author_id'))
        serializer.save(user=self.request.user, author=author)

    def perform_destroy(self, instance):
        user = self.request.user
        author = get_object_or_404(User, pk=self.kwargs.get('author_id'))
        follow = get_object_or_404(Follow, user=user, author=author)
        follow.delete()
