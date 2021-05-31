from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(null=True, blank=True, max_length=255)
    avatar = models.ImageField(null=True, blank=True)
    active_template = models.ForeignKey('products.TemplateImage', null=True, blank=True, on_delete=models.CASCADE)
