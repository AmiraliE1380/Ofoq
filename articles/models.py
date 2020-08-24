from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField('تاریخ انتشار:')

    def __str__(self):
        return self.title


class Comment(models.Model):
    reply_id = models.IntegerField(default=-1)
    username = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    pub_date = models.DateTimeField()