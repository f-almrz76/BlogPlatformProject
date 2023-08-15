from django.urls import path
from . import views
from users.admin import author_admin_site

urlpatterns = [

    path('authors/', views.author_list, name="author_list"),
    path('authors/<int:pk>/', views.author_details, name="author_details"),
    path('author_admin/', author_admin_site.urls),

]