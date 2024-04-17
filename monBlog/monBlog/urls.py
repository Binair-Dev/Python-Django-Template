from django.contrib import admin
from django.urls import path
from . import views
from article import views as article_views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home),

    path('article/create/', article_views.article_create),
    path('article/', article_views.article_list),
]
