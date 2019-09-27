from django.db import models
import datetime


# Create your models here.

class Player (models.Model):
    name        = models.CharField(max_length=10)
    nick        = models.CharField(max_length=20, null=False)
    startdate   = models.DateField(("Date"), default=datetime.date.today)
    score       = models.IntegerField(default=0)