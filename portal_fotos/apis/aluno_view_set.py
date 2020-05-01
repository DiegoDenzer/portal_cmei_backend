from rest_framework import viewsets
from rest_framework.response import Response

from portal_fotos.models.aluno_model import AlunoModel
from portal_fotos.serializers.aluno_serializer import AlunoSerializer


class AlunoViewSet(viewsets.ViewSet):
    """
    View da api responsavel por acessar dados do Aluno.
    """
    def list(self, request):
        """
        Responsavel por acessar os Albuns.
        """
        queryset = AlunoModel.objects.all()
        serializer = AlunoSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        queryset = AlunoModel.objects.filter(id=pk)
        serializer = AlunoSerializer(queryset)
        return Response(serializer.data)

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass