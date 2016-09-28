from django.conf.urls import url,include
from .views import (
    ArticleCreateAPIView,
    ArticleDeleteAPIView,
    ArticleDetailAPIView,
    ArticleListAPIView,
    ArticleUpdateAPIView,
    )



from .views import (
    CommentCreateAPIView,
    CommentListAPIView,
  )

urlpatterns = [
    url(r'^$', ArticleListAPIView.as_view(), name='list'),
    url(r'^create/$', ArticleCreateAPIView.as_view(), name='create'),
    url(r'^(?P<pk>[\w-]+)/$', ArticleDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<pk>[\w-]+)/edit/$', ArticleUpdateAPIView.as_view(), name='update'),
    url(r'^(?P<pk>[\w-]+)/delete/$', ArticleDeleteAPIView.as_view(), name='delete'),
    # url(r'^(?P<pk>[\w-]+)/comments/$', include("comments.api.urls", namespace='<comments-api></comments-api>')),

    url(r'^(?P<pk>[\w-]+)/comments/$', CommentListAPIView.as_view(), name='list'),
    url(r'^(?P<pk>[\w-]+)/comments/create/$', CommentCreateAPIView.as_view(), name='create'),
    # url(r'^(?P<pk>[\w-]+)/comments/(?P<pk>\d+)/$', CommentDetailAPIView.as_view(), name='thread'),

]