from django.urls import path , include
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authors/', views.author_list, name="author_list"),
    path('authors/<int:pk>/', views.author_details, name="author_details"),
    path('login/', views.login_view, name='login'),
    path('author_admin/', include('users.admin.author_admin.urls')),

]