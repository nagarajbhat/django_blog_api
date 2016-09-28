"""
Contains class based views
"""

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


from articles.models import Comment
from .serializers import CommentSerializer
from .serializers import CommentCreateUpdateSerializer

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

"""
class based views to create,retrieve,update,delete artilcles
"""


class ArticleCreateAPIView(CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleCreateUpdateSerializer

    # perform_create() is a method provided by CreateAPIView
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ArticleListAPIView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [AllowAny]


class ArticleDetailAPIView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsOwnerOrReadOnly]


class ArticleUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleCreateUpdateSerializer
    permission_classes = [IsOwnerOrReadOnly]

    # perform_create() is a method provided by CreateAPIView
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class ArticleDeleteAPIView(DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsOwnerOrReadOnly]

"""
class based views to create,retrieve comments
"""


class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateUpdateSerializer

    # perform_update() is a method provided by CreateAPIView
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentListAPIView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [AllowAny]


# class CommentDetailAPIView(RetrieveAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = [IsOwnerOrReadOnly]
