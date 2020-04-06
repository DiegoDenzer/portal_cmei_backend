from ..models.turma_model import TurmaModel

from rest_framework import serializers


class TurmaSerializer(serializers.ModelSerializer):

    class Meta:
        model = TurmaModel
        fields = (
            'nome',
            'data_criacao',
            'data_update',
            'ano_turma',
            'id',
            'periodo',
        )

