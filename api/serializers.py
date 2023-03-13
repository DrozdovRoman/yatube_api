from rest_framework.relations import SlugRelatedField
from rest_framework import serializers
from posts.models import Comment, Post


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(
        read_only=True,
        slug_field='username',)

    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ('pub_date',)


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username', )

    class Meta:
        model = Comment
        fields = ('__all__')
        read_only_fields = (
            'post',
            'created', )
