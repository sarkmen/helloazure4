from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=500)
    photo = models.ImageField()

    def __str__(self):
        return self.title