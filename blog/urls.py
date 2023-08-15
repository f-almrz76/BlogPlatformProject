from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('author_admin/', admin.site.urls),
    path('authors/', views.author_list, name="author_list"),
    path('authors/<int:pk>/', views.author_details, name="author_details"),
    path('login/', views.login_view, name='login'),

] 