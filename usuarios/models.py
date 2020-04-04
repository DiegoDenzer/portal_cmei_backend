from django.db import models

# Create your models here.
# Create your models here.
import uuid

from django.contrib.auth.models import AbstractUser
from django.db.models import UUIDField


class MyUser(AbstractUser):
    id = UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
