from django.contrib import admin
from .models import Author
from django.contrib.admin import AdminSite

# Register your models here.

admin.site.register(Author)

class AuthorAdminSite(AdminSite):
    site_header = "Blog Author admin"
    site_title = "Blog Author Admin Portal"

author_admin_site = AuthorAdminSite(name='author_admin')

author_admin_site.register(Author)



