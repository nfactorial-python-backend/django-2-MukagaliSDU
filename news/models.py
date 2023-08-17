from django.db import models
from django.utils import timezone


# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.title


class Comments(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now())
    news = models.ForeignKey(News, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.content}"