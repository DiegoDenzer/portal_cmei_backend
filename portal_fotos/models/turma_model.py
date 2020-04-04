from django.db import models

from portal_fotos.models.aluno_model import AlunoModel
from portal_fotos.models.base_model import BaseModel
from portal_fotos.models.educador_model import EducadorModel


class TurmaModel(BaseModel):

    nome = models.CharField(max_length=255)
    ano_turma = models.CharField(max_length=4)
    periodo = models.CharField(max_length=30)

    # Relacionamentos
    alunos = models.ForeignKey(
        AlunoModel,
        on_delete=models.CASCADE, related_name="turmas",
    )
    educadores = models.ForeignKey(
        EducadorModel,
        on_delete=models.CASCADE, related_name="turmas",
    )

    class Meta:
        db_table = 'turma'
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'
        ordering = ('-pk',)

    def __unicode__(self):
        return f'{self.nome}'