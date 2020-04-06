from rest_framework import serializers

from portal_fotos.models.album_model import AlbumModel


class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = AlbumModel
        fields = (
            'nome',
            'id',
            'descricao',
        )