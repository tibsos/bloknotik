import os

from django.db import models as m

from uuid import uuid4 as u4

from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver


def upload_avatar(instance, filename):

    file_extension = filename.split('.')[-1]

    new_filename = f"{u4}.{file_extension}"

    return os.path.join('uploads/profile/avatar', new_filename)

class Profile(m.Model):

    user = m.OneToOneField(User, on_delete = m.CASCADE, related_name = 'profile')

    name = m.CharField(max_length = 300)

    avatar = m.ImageField(upload_to = upload_avatar, null = True)

    premium = m.BooleanField(default = False)

    def __str__(self):

        return f"{self.name} | {self.user.username}"

@receiver(post_save, sender = User)
def create_user_profile(sender, instance, created, **kwargs):

    if created:
        
        Profile.objects.create(user = instance)