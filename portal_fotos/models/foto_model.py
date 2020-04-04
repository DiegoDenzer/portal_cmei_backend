from django.db import models

from portal_fotos.models.base_model import BaseModel
from portal_fotos.models.album_model import AlbumModel


class FotoModel(BaseModel):
    """
    Cada Modelo do tipo foto  possui uma descricao e uma imagem e o album
    a qual pertence
    """
    descricao = models.CharField(max_length=255)
    imagem = models.ImageField(default="/fotos/sem-foto.png", upload_to='fotos', null=True, blank=True)
    album = models.ForeignKey(
        AlbumModel, null=True,
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = 'foto'
        verbose_name = 'Foto'
        verbose_name_plural = 'Fotos'
        ordering = ('-pk',)

    def __unicode__(self):
        return f'{self.descricao}'
