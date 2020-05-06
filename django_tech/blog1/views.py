from django.shortcuts import render
from .models import Post
def add_post(request):
    qs = Post.objects.all()
    return render(request, 'blog1/post.html', { 'post_list' : qs })

def post_list(request):
    qs = Post.objects.all()
    q = request.GET.get('q', '') #없으면 ''를 반환 (검색어가 q에 저장)
    if q:
        qs = qs.filter(content__icontains=q)
    return render(request, 'blog1/post_list.html',
                  {'post_list' : qs,
                   'q' : q,
                  })