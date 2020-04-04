from django.contrib import admin

# Register your models here.
from portal_fotos.models.album_model import AlbumModel
from portal_fotos.models.aluno_model import AlunoModel
from portal_fotos.models.educador_model import EducadorModel
from portal_fotos.models.foto_model import FotoModel


@admin.register(AlunoModel)
class AlunoAdmin(admin.ModelAdmin):
    list_display = [
        "nome",
        "data_nasc",
        "idade"
    ]
    readonly_fields = ["idade"]
    search_fields = ['nome']


@admin.register(EducadorModel)
class EducadorAdmin(admin.ModelAdmin):
    list_display = [
        "nome",
        "data_nasc",
        "idade"
    ]
    readonly_fields = ["idade"]
    search_fields = ['nome']


class FotoTabular(admin.TabularInline):
    model = FotoModel


@admin.register(AlbumModel)
class AlbumAdmin(admin.ModelAdmin):
    list_display = [
        "nome",
        "descricao",
    ]
    search_fields = ['nome']
    inlines = (FotoTabular,)
