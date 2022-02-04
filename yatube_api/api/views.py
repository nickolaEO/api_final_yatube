from rest_framework import viewsets, permissions
from rest_framework.pagination import LimitOffsetPagination

from posts.models import Post, User, Group
from .serializers import PostSerializer, UserSerializer, GroupSerializer
from .permissions import IsAuthorOrReadOnlyPermissions


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsAuthorOrReadOnlyPermissions
    )
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
