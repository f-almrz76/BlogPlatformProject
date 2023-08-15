from django.urls import path
from . import views
from .admin import AuthorAdmin
from .models import Author
from django.contrib import admin

# admin.site.register(Author, AuthorAdmin)

urlpatterns = [

    path('authors/', views.author_list, name="author_list"),
    path('authors/<int:pk>/', views.author_details, name="author_details"),
    path('login/', views.login_view, name='login'),
    path('author_admin/', admin.site.urls)
]