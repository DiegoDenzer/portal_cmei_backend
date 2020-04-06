from rest_framework import serializers

from portal_fotos.models.aluno_model import AlunoModel


class AlunoSerializer(serializers.ModelSerializer):

    class Meta:
        model = AlunoModel
        fields = (
            'nome',
            'data_nasc',
            'id',
        )