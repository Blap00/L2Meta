from django.db import models
from django.utils import timezone

# Create your models here.

class News(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    fechaSubida = models.DateField(default=timezone.now().date())

    def __str__(self):
        return self.title

class NewsImage(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"Image for {self.news.title}"

