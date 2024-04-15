from django.contrib import admin
from django.urls import path
from books import views

urlpatterns = [
    path('', views.book_list),
    path('<int:id>/', views.book_one)
]
