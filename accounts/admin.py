from django.contrib import admin
from .models import MedicalWorker,Department
from django.contrib.auth.admin import UserAdmin
# Register your models here.


class AccountUserAdmin(UserAdmin):
    ordering = ('name',)

class AccountAdmin(AccountUserAdmin):
    list_display=('email','is_active','is_staff','name','last_login','date_joined')
    search_fields=('email','name','phone')
    readonly_fields=('last_login','date_joined')
    filter_horizontal=()
    list_filter=()
    fieldsets=()

admin.site.register(MedicalWorker,AccountAdmin)
admin.site.register(Department)
