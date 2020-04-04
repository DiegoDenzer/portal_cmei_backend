from portal_fotos.models.pessoa_model import PessoaModel


class EducadorModel(PessoaModel):
    """
    Classe para educadores (Professores).
    """
    class Meta:
        db_table = 'educador'
        verbose_name = 'Educador'
        verbose_name_plural = 'Educadores'

    def __unicode__(self):
        return f'{self.nome}'

