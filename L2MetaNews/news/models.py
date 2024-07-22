from django.db import models
from django.utils import timezone
import os

# Create your models here.


#Testing
def news_image_upload_path(instance, filename):
    # Construye la ruta de carga basada en el título de la noticia y el nombre del archivo
    return os.path.join(instance.news.title, filename)

class NewsCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class News(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    detallesAdicionales = models.TextField(null=True,blank=True)
    youtube_adicional = models.CharField(max_length=255, null=True, blank=True)
    fechaSubida = models.DateField(default=timezone.now().date())
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title
    
    def youtube_embed_url(self):
        if self.youtube_adicional:
            if "youtube.com/watch?v=" in self.youtube_adicional:
                return self.youtube_adicional.replace("watch?v=", "embed/")
            elif "youtu.be" in self.youtube_adicional:
                video_id = self.youtube_adicional.split("/")[-1]
                return f"https://www.youtube.com/embed/{video_id}"
            elif "youtube.com/embed/" in self.youtube_adicional:
                return self.youtube_adicional
        return ""

class NewsImage(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=news_image_upload_path)

    def __str__(self):
        return f"Image for {self.news.title}"
