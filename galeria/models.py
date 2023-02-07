from django.db import models


# Create your models here.
class Fotografia(models.Model):
    titulo = models.CharField(max_length=100, blank=False, null=False)
    tag = models.CharField(max_length=100, blank=False, null=False, default='tag')
    legenda = models.CharField(max_length=150, blank=False, null=False)
    descricao = models.TextField(max_length=500, blank=False, null=False)
    imagem = models.ImageField(upload_to='fotos')

    def __str__(self):
        return self.titulo, self.tag, self.legenda