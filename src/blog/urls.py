from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import BlogHome, BlogPostCreate, BlogPostEdit, BlogPostDetail, BlogPostDelete

app_name = "blog"

urlpatterns = [
    path('', BlogHome.as_view(), name="home"),
    path('create/', login_required(BlogPostCreate.as_view()), name="create"),
    path('<str:slug>/', BlogPostDetail.as_view(), name="post"),
    path('edit/<str:slug>/', BlogPostEdit.as_view(), name="edit"),
    path('delete/<str:slug>/', BlogPostDelete.as_view(), name="delete"),
]
