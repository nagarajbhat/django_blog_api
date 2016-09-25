from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView)

from articles.models import Article
from .serializers import ArticleSerializer
from .permissions import IsOwnerOrReadOnly


class ArticleMixin(object):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def pre_save(self, obj):
        obj.owner = self.request.user


class ArticleListAPIView(ArticleMixin, ListAPIView):
    pass


class ArticleDetailAPIView(ArticleMixin, RetrieveAPIView):
    pass

class ArticleCreateAPIView(ArticleMixin, CreateAPIView):
    pass

class ArticleUpdateAPIView(ArticleMixin, RetrieveUpdateAPIView):
    pass

class ArticleDeleteAPIView(ArticleMixin, DestroyAPIView):
    pass
