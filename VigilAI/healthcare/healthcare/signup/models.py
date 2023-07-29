from django.db import models
# Create your models here.
class Signup(models.Model):
    name = models.CharField(max_length=50)
    token = models.CharField(max_length=50)