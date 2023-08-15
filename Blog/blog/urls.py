from django.urls import path
from .views import home, post_list,category_details,category_list, PostDetailView, UpdateComment

app_name='blog'

urlpatterns = [
    path('', home, name="home"),
    path('post/', post_list, name="post_list"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post_details"),
    path('categories/', category_list, name="category_list"),
    path('categories/<int:pk>/', category_details, name="category_details"),
    path('comment_update/<int:pk>',UpdateComment.as_view(),name='comment_update'),

]