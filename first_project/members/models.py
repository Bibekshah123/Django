from django.db import models

# Create your models here.
class Members(models.Model):
    firstname = models.CharField(max_length=225)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField()
    joined_date = models.DateField()