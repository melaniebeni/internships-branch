from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('posts', views.posts, name="posts"),
    path('create', views.create, name='create')
]