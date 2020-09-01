from django.core.management.base import BaseCommand

from authapp.models import ShopUser, ShopUserProfile


class Command(BaseCommand):
    users = ShopUser.objects.all()
    for user in users:
        user_profile = ShopUserProfile.objects.create(user=user)
        user_profile.save()