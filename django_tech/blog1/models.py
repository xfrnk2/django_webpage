from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)

    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) #db 저장시간
    updated_at = models.DateTimeField(auto_now=True) # 수정시간
    photo = models.ImageField(blank=True)
    is_public = models.BooleanField(default=False, verbose_name='공개여부') #

    def __str__(self): # 자바의 to string과 유사
        # return f" Custom Post object ({self.id})"
        return f"{self.title}"

    # def title_length(self): # 인자없는 속성, 인자없는 함수만 가능(admin.py로부터 function으로 호출 될 경우)
    #     python의 경우 @property로도 정의가능
    #
    #     return len(self.title)
    # title_length.short_description = "타이틀 글자수" # 컬럼의 표시되는 부분을 설정할 수 있다. 여기말고 admin.py에 구현도 가능

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)