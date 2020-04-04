from django.db import models

from portal_fotos.models.base_model import BaseModel
from portal_fotos.models.turma_model import TurmaModel


class AlbumModel(BaseModel):
    # Fields
    nome = models.CharField(max_length=255)
    descricao = models.TextField(max_length=5000)
    turma = models.ForeignKey(
        TurmaModel,
        on_delete=models.CASCADE, related_name="albums",
    )

    class Meta:
        ordering = ('-pk',)
        db_table = 'album'
        verbose_name = 'Album'
        verbose_name_plural = 'Albuns'

    def __unicode__(self):
        return f'{self.nome}'

    def __str__(self):
        return  f'{self.nome}'
