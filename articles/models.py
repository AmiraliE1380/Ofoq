from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('تاریخ انتشار:')


class Comment(models.Model):
    reply_id = models.IntegerField()
    username = models.CharField(max_length=100)
    content = models.CharField()
