from django.contrib import admin
from .models import Author
from django.contrib.admin import AdminSite

# Register your models here.
class AuthorAdminSite(AdminSite):
    site_header = 'Custom Author Admin'
    site_title = 'Custom Author Admin Panel'
    index_title = 'Welcome to Author Admin Panel'


author_admin_site = AuthorAdminSite(name='author_admin')


@admin.register(Author, site=author_admin_site)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')

    search_fields = ('name', 'email')

admin.site.register(Author, AuthorAdmin)


