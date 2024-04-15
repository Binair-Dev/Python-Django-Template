from django.contrib import admin
from django.urls import path, include
from article import views as views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('books/', include('books.urls'))
]
