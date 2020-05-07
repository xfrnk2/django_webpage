from django.contrib import admin
from django.utils.safestring import mark_safe

from . models import Post, Comment, Tag
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    def photo_tag(self, post):
        if post.photo:
            return mark_safe(f'<img src="{post.photo.url}" style="width : 72px;" />')
        return None