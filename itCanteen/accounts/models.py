from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.TextField(max_length=10, null=True)
    email = models.TextField(null=True)
    register_date_time = models.DateTimeField(null=True)
    status = models.BooleanField(default=False)
    is_validated = models.BooleanField(default=False)
    real_first_name = models.TextField(null=True)
    real_last_name = models.TextField(null=True)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(create_user_profile, sender=User)
