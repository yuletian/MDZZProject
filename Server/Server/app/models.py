"""
Definition of models.
"""

from django.db import models

# Create your models here.
class TestTable(models.Model):
    name = models.CharField(max_length = 123)