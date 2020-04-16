from django.shortcuts import render
from .models import Post
def add_post(request):
    qs = Post.objects.all()
    return render(request, 'blog1/post.html', { 'post_list' : qs })