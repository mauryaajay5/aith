from django.db import models

# Create your models here.
class db(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=30)
    desc=models.CharField(max_length=120)
    date=models.DateField()


def __str__(self):
    return self.name

