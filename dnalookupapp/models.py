from django.db import models

# Create your models here.
class Protein(models.Model):
    name = models.CharField(max_length=255)
    ref = models.CharField(max_length=255)
    seq = models.TextField()

    def __str__(self):
        return self.name + ' ' + self.seq