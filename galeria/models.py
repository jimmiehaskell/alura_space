from datetime import datetime
from django.db import models


# Create your models here.

class Fotografia(models.Model):

    OPCOES_CATEGORIA = [
        ("NEBULOSA", "Nebulosa"),
        ("ESTRELA", "Estrela"),
        ("GALÁXIA", "Galáxia"),
        ("PLANETA", "Planeta"),
    ]

    nome = models.CharField(
        blank=False,
        max_length=100,
        null=False,
    )
    legenda = models.CharField(
        blank=False,
        max_length=150,
        null=False,
    )
    categoria = models.CharField(
        blank=False,
        choices=OPCOES_CATEGORIA,
        default='',
        max_length=10,
    )
    descricao = models.TextField(
        blank=False,
        null=False,
        verbose_name='Descrição',
    )
    foto = models.ImageField(
        blank=True,
        upload_to="fotos/%Y/%m/%d/",
    )
    publicada = models.BooleanField(
        default=False,
    )

    data_fotografia = models.DateTimeField(
        default=datetime.now,
        blank=False
    )

    def __str__(self):
        return f"{self.nome}"
