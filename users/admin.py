from django.contrib import admin
from django.contrib.admin import AdminSite

from .models import Author
# Register your models here.

admin.site.register(Author)
author_admin_site = AdminSite(name='author_admin')
