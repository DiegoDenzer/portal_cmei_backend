from requests import Response
from rest_framework import viewsets

from portal_fotos.models.turma_model import TurmaModel
from portal_fotos.serializers.turma_serializer import TurmaSerializer


class TurmaViewSet(viewsets.ViewSet):
    """
    View da api responsavel por acessar dados da Turma.
    """
    def list(self, request):
        """
        Responsavel por acessar as Turmas do Usuario.
        """
        queryset = TurmaModel.objects.all()
        serializer = TurmaSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        queryset = TurmaModel.objects.filter(id=pk)
        serializer = TurmaSerializer(queryset, many=True)
        return Response(serializer.data)

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass