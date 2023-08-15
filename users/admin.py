from django.contrib import admin
from .models import Author
from django.contrib.admin import AdminSite

# Register your models here.

class AuthorAdminSite(AdminSite):
    site_header = 'Author Administration'
    site_title = 'Author Admin Site'

author_admin_site = AuthorAdminSite(name='author_admin')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)




