from rest_framework import serializers
from articles.models import Article
from articles.models import Comment

from accounts.api.serializers import UserDetailSerializer


class ArticleCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['title', 'body']


class ArticleSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer(read_only=True)

    class Meta:
        model = Article
        fields = ['title', 'body', 'user']

class ArticleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [
            'title',
            'body',
        ]



class CommentCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['text','article']


class CommentSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer(read_only=True)
    article = ArticleDetailSerializer()
    class Meta:
        model = Comment
        fields = ['text', 'user','article']
