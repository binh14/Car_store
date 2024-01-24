from django.db import models

# Create your models here.
class Car(models.Model):
    id = models.IntegerField
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)

    def __str__(self):
        return self.name
