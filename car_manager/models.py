from django.db import models


class Car(models.Model):
    model = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    year = models.IntegerField()
    engine = models.CharField(max_length=50)
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.model
