from django.urls import path
from .views import home, post_list,post_details,category_details,category_list, comment_update
from . import views

app_name='blog'

urlpatterns = [
    path('', home, name="home"),
    path('post/', post_list, name="post_list"),
    path('post/<int:pk>/', views.PostDetailView.as_veiw(), name="post_details"),
    path('categories/', category_list, name="category_list"),
    path('categories/<int:pk>/', category_details, name="category_details"),
    path('comment_update/<int:pk>',views.CommentUpdateView.as_view(),name='comment_update'),

]