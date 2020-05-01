from rest_framework import viewsets
from rest_framework.response import Response

from portal_fotos.models.educador_model import EducadorModel
from portal_fotos.serializers.educador_serializer import EducadorSerializer


class EducadorViewSet(viewsets.ViewSet):
    """
    View da api responsavel por acessar dados do Aluno.
    """
    def list(self, request):
        """
        Responsavel por acessar os Albuns.
        """
        queryset = EducadorModel.objects.all()
        serializer = EducadorSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        queryset = EducadorModel.objects.filter(id=pk)
        serializer = EducadorSerializer(queryset)
        return Response(serializer.data)

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass