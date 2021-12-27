
from django.urls import path
from . import views
from .views import (
    PostListView,
)

urlpatterns = [
    path('post/', PostListView.as_view(), name='blog-home'),
    path('post/<int:id>/', views.post_detail_view, name='post-detail'),
    path('about/', views.about, name='blog-about'),
    path('images/', views.images, name='blog-images'),
]
