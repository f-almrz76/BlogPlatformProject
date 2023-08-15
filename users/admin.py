from django.contrib import admin
from .models import Author
from django.contrib.admin import AdminSite

# Register your models here.

# admin.site.register(Author)



class MyAdminSite(AdminSite):
    site_header = "Author Site"

author_admin_site = MyAdminSite(name="myadmin")
author_admin_site.register(Author)