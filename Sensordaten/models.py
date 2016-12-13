from django.db import models

# Create your models here.

class Sensorkits (models.Model):
    besitzer = models.CharField(max_length=200, default="Hans")
    co2 = models.FloatField(max_length=200)
    vluftTemp = models.FloatField(max_length=200)
    abgTemp = models.FloatField(max_length=200)

    def __str__(self):
        return str(self.besitzer) + 'mit Co2 Wert:' + str(self.co2)

class Kunden (models.Model):
    vorname = models.CharField(max_length=250)
    nachname = models.CharField(max_length=250)
    straße = models.CharField (max_length=250)
    hausnummer = models.CharField(max_length=20)
    sensorkit = models.ForeignKey(Sensorkits, on_delete=models.CASCADE)
    earlybirduser = models.BooleanField(default=False)

    def __str__(self):
        return self.vorname + ' , ' + self.nachname