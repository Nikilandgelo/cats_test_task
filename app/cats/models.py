from cats_project.mixins import UUIDMixin
from django.db import models
from cats_type.models import CatsType
from User.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Cat(UUIDMixin):
    color = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    type = models.ForeignKey(CatsType, on_delete=models.CASCADE,
                             related_name='cats')
    score = models.ManyToManyField(User, through='UsersCatsScore')
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name='cats')

    def __str__(self) -> str:
        return (f'{self.owner.username} cat`s with color '
                f'{self.color} and {self.age} full months old')


class UsersCatsScore(UUIDMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='cats_scores')
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE,
                            related_name='scores')
    score = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    class Meta:
        unique_together = ('user', 'cat')
