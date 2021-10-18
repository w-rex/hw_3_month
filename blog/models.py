from django.db import models

# Create your models here.


class Blog(models.Model):
    image = models.FileField(upload_to='blog_images/', default=True)
    title = models.CharField(max_length=120)
    reposts = models.IntegerField(default=0)
    description = models.TextField()
    likes = models.IntegerField(default=0)


class Comments(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=150)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)


