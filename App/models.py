from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=90, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    password = models.CharField(max_length=256, null=False, blank=False)
    repeat_password = models.CharField(max_length=256, null=False, blank=False)
def __str__(self):
        return self.username