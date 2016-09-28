from rest_framework import serializers
from articles.models import Article
from articles.models import Comment

from accounts.api.serializers import UserDetailSerializer

#used by ArticleCreateAPIView,ArticleUpdateAPIView
class ArticleCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['title', 'body']

#used by ArticleListAPIView,ArticleDetailAPIView,ArticleDestroyAPIView
class ArticleSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer(read_only=True)

    class Meta:
        model = Article
        fields = ['title', 'body', 'user']

#This is used by CommentSerializer to display contents of the article to which the comment belongs to
class ArticleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [
            'title',
            'body',
        ]


#used by CommentCreateAPIView
class CommentCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['text','article']

#used by CommentListAPIView
class CommentSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer(read_only=True)
    article = ArticleDetailSerializer()
    class Meta:
        model = Comment
        fields = ['text', 'user','article']
