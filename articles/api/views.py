from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView)

from articles.models import Article
from .serializers import ArticleSerializer
from .serializers import ArticleCreateUpdateSerializer
from .permissions import IsOwnerOrReadOnly


class ArticleMixin(object):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def pre_save(self, obj):
        obj.user = self.request.user


class ArticleCU(object):
    queryset = Article.objects.all()
    serializer_class = ArticleCreateUpdateSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def pre_save(self, obj):
        obj.user = self.request.user


class ArticleListAPIView(ArticleMixin, ListAPIView):
    pass


class ArticleDetailAPIView(ArticleMixin, RetrieveAPIView):
    pass


class ArticleCreateAPIView(ArticleCU, CreateAPIView):
    pass


class ArticleUpdateAPIView(ArticleCU, RetrieveUpdateAPIView):
    pass


class ArticleDeleteAPIView(ArticleMixin, DestroyAPIView):
    pass
