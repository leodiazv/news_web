from distutils.command.upload import upload
from django.db import models
from django import forms

# Create your models here.
class News(models.Model):
    image = models.ImageField(upload_to='images/',verbose_name='Imagen', null=True)
    title = models.CharField(max_length=100, verbose_name='Titulo')
    description = models.TextField(verbose_name='Descripción', null=True)
    

    
    def __str__(self) -> str:
        fila = "Titulo: " + self.title
        return fila

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()