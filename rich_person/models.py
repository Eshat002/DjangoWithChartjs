# charts/models.py
from django.db import models

class RichPerson(models.Model):
    name = models.CharField(max_length=100)
    wealth = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return self.name
