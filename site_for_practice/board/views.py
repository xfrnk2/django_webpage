from django.shortcuts import render
from . models import Post

# Create your views here.

def post_list(request):
    # 순서 : render(리퀘스트, 템플릿 위치, 전달 인자)
    qs = Post.objects.all()
    return render(request, 'board/post_list.html', {'post_list' : qs})