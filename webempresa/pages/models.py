from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Page(models.Model):
    tittle = models.CharField(verbose_name="Título", max_length=200)
    content = RichTextField(verbose_name="Contenido")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Edición")

    class Meta:
        verbose_name = "Página"
        verbose_name_plural = "Páginas"
        ordering = ['tittle']

    def __str__(self):
        return self.tittle
