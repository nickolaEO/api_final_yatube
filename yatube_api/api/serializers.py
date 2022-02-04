from rest_framework import serializers
from rest_framework.relations import SlugRelatedField


from posts.models import Comment, Post, User, Group


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'username', 'first_name', 'last_name', 'posts')
        model = User


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = ('id', 'text', 'pub_date', 'author', 'image', 'group')
        model = Post


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'slug', 'description')
        model = Group


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment
