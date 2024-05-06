from django.db import models

# Create your models here.

class Ranking(models.Model):
    name = models.CharField(max_length=255)
    elapsed_time = models.TimeField()