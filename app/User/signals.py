from django.db.models.signals import post_save
from django.dispatch import receiver
from User.models import User
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=User)
def create_token(sender: User, instance: User, created: bool, **kwargs):
    if created:
        Token.objects.create(user=instance)
