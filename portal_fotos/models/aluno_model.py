from django.urls import reverse
from django.db import models as models

from portal_fotos.models.pessoa_model import PessoaModel


class AlunoModel(PessoaModel):
    """
    Classe Aluno.S
    """
    class Meta:
        db_table = 'aluno'
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'

    def __unicode__(self):
        return f'{self.nome}'

    def __str__(self):
        return f'{self.nome}'
