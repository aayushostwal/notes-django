from pyexpat import model
from statistics import mode
from django.db import models


# Create your models here.

class TakeNotes(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(blank=True, null=True)
    date_time = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ('-date_time', )

