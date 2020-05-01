from django.db import models

from portal_fotos.models.aluno_model import AlunoModel
from portal_fotos.models.base_model import BaseModel
from portal_fotos.models.educador_model import EducadorModel


class TurmaModel(BaseModel):

    nome = models.CharField(max_length=255)
    ano_turma = models.CharField(max_length=4)
    periodo = models.CharField(max_length=30)

    class Meta:
        db_table = 'turma'
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'
        ordering = ('-pk',)

    def __unicode__(self):
        return f'{self.nome}'


class TurmaAlunoModel(BaseModel):
    turma = models.ForeignKey(
        TurmaModel,
        on_delete=models.CASCADE, related_name="turmas",
    )
    aluno = models.ForeignKey(
        AlunoModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.aluno.nome

    class Meta:
        db_table = 'turma_x_aluno'
        verbose_name = "Aluno"
        verbose_name_plural = "Alunos"


class TurmaEducadorModel(BaseModel):
    turma = models.ForeignKey(
        TurmaModel,
        on_delete=models.CASCADE, related_name="turmas_educador",
    )
    educador = models.ForeignKey(
        EducadorModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.educador.nome

    class Meta:
        db_table = 'turma_x_educador'
        verbose_name = "Educador"
        verbose_name_plural = "Educadores"
