from django.contrib import admin
from .models import News, NewsImage, NewsCategory

# Register your models here.

class NewsImageInline(admin.TabularInline):
    model = NewsImage
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    model =NewsCategory

admin.site.register(NewsCategory, CategoryAdmin)

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'fechaSubida')  # Campos que se mostrarán en la lista de noticias
    search_fields = ['title']  # Campos por los que se puede buscar en la interfaz de administración
    fields = ('title', 'description', 'detallesAdicionales', 'youtube_adicional', 'fechaSubida', 'category')
    inlines = [NewsImageInline]  # Para mostrar las imágenes asociadas en el formulario de News

admin.site.register(News, NewsAdmin)


