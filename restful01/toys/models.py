from django.db import models
from datetime import date

# Create your models here.
class Toy(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=150, blank=False, default='')
    description = models.CharField(max_length=250, blank=False, default='')
    toy_category = models.CharField(max_length=200, blank=False, default='')
    release_date = models.DateTimeField()
    was_included_in_home = models.BooleanField(default=False)

    class Meta:
        ordering = ('name',)

class One(models.Model):
    one = models.IntegerField()

    class Meta:
        db_table = 'OneTwo'

class Two(models.Model):
    two = models.IntegerField()

    class Meta:
        db_table = 'OneTwo'