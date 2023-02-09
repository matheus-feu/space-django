from datetime import datetime
from django.db import models
from stdimage.models import StdImageField

class Fotografia(models.Model):
    """Modelo de Fotografia, contém as informações de cada fotografia"""

    OPCOES_CATEGORIA = [
        ("Nebulosa", "NEBULOSA"),
        ("Estrela", "ESTRELA"),
        ("Galáxia", "GALÁXIA"),
        ("Planeta", "PLANETA"),
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='')
    descricao = models.TextField(null=False, blank=False)
    foto = StdImageField('Fotografia', upload_to='fotos/%Y/%m/%d/',
                                variations={'thumbnail': {'width': 500, 'height': 500, 'crop': True}})
    publicada = models.BooleanField(default=False)
    data_publicacao = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        verbose_name = 'Fotografia'
        verbose_name_plural = 'Fotografias'

    def __str__(self):
        return self.nome + " - " + self.categoria + " - " + self.legenda
