from django.contrib import admin
from .models import UserModel, ContactModel, ServiceOption, \
StandartOption, DetailsOption, ServiceModel, OurWorksModel, VisitHistory
# User Model Admin
@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username']
    list_display_links = ['id', 'username']
    search_fields = ['username']

@admin.register(VisitHistory)
class VisitHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'ip_address', 'timestamp')
    list_filter = ('user', 'timestamp', 'ip_address')
    search_fields = ('user__username', 'ip_address')
    readonly_fields = ('user', 'ip_address')

@admin.register(ServiceOption)
class ServiceOptionAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(ServiceModel)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    search_fields = ['title']

@admin.register(DetailsOption)
class DetailsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']

@admin.register(StandartOption)
class StandartAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']

@admin.register(OurWorksModel)
class OurWorksAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    search_fields = ['title']

@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'service', 'message')


admin.site.site_header = 'Mikond Administration'
admin.site.site_title = 'Mikond'