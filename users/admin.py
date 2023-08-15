from django.contrib import admin
from .models import Author
from django.contrib.admin import AdminSite

# Register your models here.

class AuthorAdminSite(AdminSite):
    site_header = 'New Admin Panel for Authors'
    site_title = 'HELLO AUTHORS!'

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name')

admin.site.register(Author, AuthorAdmin)
