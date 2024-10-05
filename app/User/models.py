from cats_project.mixins import UUIDMixin
from django.contrib.auth.models import AbstractUser


class User(UUIDMixin, AbstractUser):
    pass

    # related fields
    # - cats_scores
    # - cats
