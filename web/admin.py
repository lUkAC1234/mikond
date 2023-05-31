# --------------------------------------------------------------------------- #
# Django exceptions
from django.contrib import admin
# --------------------------------------------------------------------------- #
# Models and Forms
from .models import UserModel, ProjectsModel, CategoryModel, \
    CollectionsCategoryModel, CollectionsModel, ContactUSModel, LogoModel
# --------------------------------------------------------------------------- #
# Translation
from django.utils.translation import gettext_lazy as _
# --------------------------------------------------------------------------- #
# For saving html code
from django.utils.safestring import mark_safe


# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #
# User Model Admin
@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username']
    list_display_links = ['id', 'username']
    search_fields = ['username']

@admin.register(LogoModel)
class LogoAdmin(admin.ModelAdmin):
    list_display = ['id', 'logo']
    list_display_links = ['id', 'logo']
    search_fields = ['logo']

@admin.register(ProjectsModel)
class ProjectsModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'updated_at']
    list_display_links = ['id', 'title']
    search_fields = ['title']

@admin.register(CollectionsModel)
class CollectionsModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'updated_at']
    list_display_links = ['id', 'title']
    search_fields = ['title']

@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']

@admin.register(CollectionsCategoryModel)
class CollectionsCategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']

@admin.register(ContactUSModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']
    readonly_fields = ['user']

admin.site.site_header = 'Mikond'
admin.site.site_title = 'Mikond'
