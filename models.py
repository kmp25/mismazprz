from django.db import models

# Create your models here.

class Podmiot(models.Model):
    id = models.AutoField(primary_key=True)
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=100)
    def __str__(self):
        return self.nazwisko+" "+self.imie