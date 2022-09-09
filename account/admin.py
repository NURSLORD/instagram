from django.contrib import admin

from account.models import User


# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'email']
    list_display_links = list_display
    save_on_top = True
