from django.contrib import admin
from .models import Author
from django.contrib.admin import AdminSite


# @admin.register(Author)
class AuthorAdminSite(AdminSite):
    site_header = "Author Admin Panel"
    site_title = "Author Admin Panel"
    index_title = "Welcome to the Author Admin Panel"

author_admin_site = AuthorAdminSite(name='author_admin')

author_admin_site.register(Author)