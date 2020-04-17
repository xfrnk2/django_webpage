from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) #db 저장시간
    updated_at = models.DateTimeField(auto_now=True) # 수정시간
    photo = models.ImageField(blank=True)

    def __str__(self): # 자바의 to string과 유사
        # return f" Custom Post object ({self.id})"
        return self.content