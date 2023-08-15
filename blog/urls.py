from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('post/', post_list, name="post_list"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post_details"),
    path('categories/', category_list, name="category_list"),
    path('categories/<int:pk>/', category_details, name="category_details"),
    path('comment/<int:pk>/update/',CommentUpdateView.as_view(),name='update'),


]