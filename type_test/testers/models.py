from django.db import models


class Tester(models.Model):
    t_name = models.CharField(max_length=100)
    t_answer = models.IntegerField(default=0)

    def __str__(self):
        return self.t_name

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    comment = models.TextField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)