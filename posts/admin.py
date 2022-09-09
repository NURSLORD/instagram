from django.contrib import admin

from posts.models import Post


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['owner', 'image', 'is_posted']
    list_display_links = ['owner', 'is_posted']
    ordering = ['is_posted']
    search_fields = ['owner']
    save_on_top = True