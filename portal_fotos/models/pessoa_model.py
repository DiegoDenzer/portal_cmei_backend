from datetime import date

from portal_fotos.models.base_model import BaseModel

from django.db import models


class PessoaModel(BaseModel):
    nome = models.CharField(max_length=255, verbose_name='Nome')
    data_nasc = models.DateField(verbose_name='Data Nascimento')

    class Meta:
        abstract = True

    def __str__(self):
        return  f'{self.nome}'

    @property
    def idade(self):
        hoje = date.today()
        try:
            aniversario = self.data_nasc.replace(year=hoje.year)
        except ValueError:  # Fevereiro 29
            aniversario = self.data_nasc.replace(year=hoje.year, month=hoje.month + 1, day=1)
        if aniversario > hoje:
            return hoje.year - self.data_nasc.year - 1
        else:
            return hoje.year - self.data_nasc.year
