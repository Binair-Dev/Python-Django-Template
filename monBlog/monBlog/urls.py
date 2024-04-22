from django.contrib import admin
from django.urls import path
from article import views as article_views
from users import views as users_views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', article_views.article_list, name='article_list'),#Nommer pour rediriger avec un "redirect()"
    path('article/<int:id>/', article_views.article_one),
    path('article/create/', article_views.article_create, name='article_create'),
    path('author/create/', article_views.author_create, name='author_create'),
    path('article/update/<int:id>/', article_views.article_update),
    path('article/delete/<int:id>/', article_views.article_delete),
    path('article/delete/all/', article_views.article_deleteall),

    path('users/', users_views.users, name='users'),
    path('register/', users_views.register, name='register'),
    path('login/', users_views.login_view, name='login'),
    path('logout/', users_views.logout_view, name='logout'),
]
