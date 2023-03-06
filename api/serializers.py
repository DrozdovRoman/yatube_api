from rest_framework import serializers


class PostSerializer(serializers.Serializer):
    author = serializers.CharField(max_length=200)
    text = serializers.CharField(max_length=5000)
    pub_date = serializers.DateTimeField()


class Commentserializer(serializers.Serializer):
    author = serializers.CharField(max_length=200)
    post = serializers.IntegerField()
    text = serializers.CharField(max_length=5000)
    created = serializers.DateTimeField()
