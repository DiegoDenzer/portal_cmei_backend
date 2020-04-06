from rest_framework import serializers

from portal_fotos.models.educador_model import EducadorModel


class EducadorSerializer(serializers.ModelSerializer):

    class Meta:
        model = EducadorModel
        fields = (
            'pk',
            'nome',
            'data_criacao',
            'data_update',
            'id',
            'data_nasc',
        )