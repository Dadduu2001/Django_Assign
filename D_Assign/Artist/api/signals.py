from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from Artist.models import Artist_t
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=User)
def create_Artist(sender, instance=None, created=False, **kwargs):
    if created:
        Artist_t.objects.create(name=instance.username, user=instance)

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)