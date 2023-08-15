from django.contrib import admin
from .models import Author
from django.contrib.admin import AdminSite


class AuthorAdminSite(AdminSite):
    site_header = 'Author Admin Panel'
    site_title = 'Author Admin'

author_admin_site = AuthorAdminSite(name='author_admin')
