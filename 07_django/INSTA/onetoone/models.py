from django.db import models


class User(models.Model):
    email = models.CharField(max_length=100, default='', unique=True)
    password = models.CharField(max_length=50, default='')


class Profile(models.Model):
    u = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
