from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Post, Comment
# Register your models here.
# admin.site.register(Post)

# class PostAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(Post, PostAdmin)

@admin.register(Post) # Wrapping / 강사님 애용
class PostAdmin(admin.ModelAdmin):
   list_display = ['title', 'content', 'title_length', 'is_public', 'created_at', 'updated_at'] # function도 넣을 수 있다. ex)models.py의 title_length
   list_display_links = ['content'] # 기본적으로 첫번째 컬럼에 링크가 잡혀있으나, 대상을 설정할 수 있다.(여러개도 가능)
   search_fields = ['title']
   list_filter = ['created_at', 'is_public'] # 이부분도 커스텀 가능
   def title_length(self, post): # 이름을 list_display 내의 원소와 맞춘다.
      # return len(post.title)
      return f"{len(post.title)} 글자"
   def photo_tag(self, post):
      if post.photo:
            return mark_safe(f'<img src="{post.photo.url}" style="width : 72px;" />')
      return None

# @admin.register(Comment)
# class CommentAdmin(admin.CommentAdmin):
#    pass