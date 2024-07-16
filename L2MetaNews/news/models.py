from django.db import models
from django.utils import timezone
import os

# Create your models here.

def news_image_upload_path(instance, filename):
    # Construye la ruta de carga basada en el título de la noticia y el nombre del archivo
    return os.path.join('uploads/news', instance.news.title, filename)

class NewsCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class News(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    fechaSubida = models.DateField(default=timezone.now().date())
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title

class NewsImage(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=news_image_upload_path)

    def __str__(self):
        return f"Image for {self.news.title}"

