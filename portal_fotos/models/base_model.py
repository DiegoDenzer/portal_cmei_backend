import uuid

from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(default=uuid.uuid4(), primary_key=True, editable=False)
    data_criacao = models.DateTimeField(auto_now_add=True, editable=False)
    data_edicao = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True
