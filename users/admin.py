from django.contrib import admin
from .models import Author
from django.contrib.admin import AdminSite

# Register your models here.

class author_admin_site(admin.ModelAdmin):
    list_display = ('name', 'biography')
    search_fields = ('name', 'biography')

admin.site.register(Author, author_admin_site)



