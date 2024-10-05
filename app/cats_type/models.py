from cats_project.mixins import UUIDMixin
from django.db import models


class CatsType(UUIDMixin):
    name = models.CharField(max_length=225, unique=True)

    # related fields
    # - cats

    def __str__(self) -> str:
        return self.name
