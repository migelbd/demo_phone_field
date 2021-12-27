from django.db import models

from phone_field import PhoneField


class Profile(models.Model):
    name = models.CharField(max_length=128)
    phone = PhoneField()