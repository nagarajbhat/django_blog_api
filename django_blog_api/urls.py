"""django_blog_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from rest_framework_jwt.views import obtain_jwt_token
from .views import HomeView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('rest_framework_docs.urls')),
    # url(r'^', HomeView.as_view(),name='home'),
    url(r'^api/auth/token/', obtain_jwt_token),
    url(r'^api/users/', include("accounts.api.urls", namespace='users-api')),
    url(r'^api/articles/', include("articles.api.urls", namespace='articles-api')),
    url(r'^docs/', include('rest_framework_docs.urls')),



]

"""
rest_framework_docs(drf docs) genetrates API documentation by providing API's in this application.
the default template has been modified to include more content.This is done by creating 
rest_framework_docs/docs.html in templates and overriding the default template, 

moredocs.html in template extends over docs.html
"""

"""
api codes for articles and comments are in articles/api
"""