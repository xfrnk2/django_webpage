from django.contrib import admin
from .models import Post
# Register your models here.
# admin.site.register(Post)

# class PostAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(Post, PostAdmin)

@admin.register(Post) # Wrapping / 강사님 애용
class PostAdmin(admin.ModelAdmin):
   pass

