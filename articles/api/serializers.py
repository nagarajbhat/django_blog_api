from rest_framework import serializers
from articles.models import Article

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
