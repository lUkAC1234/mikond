from django.contrib import admin
from .models import UserModel, ContactModel, ServiceOption
# User Model Admin
@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username']
    list_display_links = ['id', 'username']
    search_fields = ['username']

@admin.register(ServiceOption)
class ServiceOptionAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'service', 'message')