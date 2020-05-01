from rest_framework import viewsets
from rest_framework.response import Response

from portal_fotos.models.album_model import AlbumModel
from portal_fotos.serializers.album_serializer import AlbumSerializer


class AlbumViewSet(viewsets.ViewSet):
    """
    View da api responsavel por acessar dados do album.
    """
    def list(self, request):
        """
        Responsavel por acessar os Albuns.
        """
        queryset = AlbumModel.objects.all()
        serializer = AlbumSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        queryset = AlbumModel.objects.filter(id=pk)
        serializer = AlbumSerializer(queryset)
        return Response(serializer.data)

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass