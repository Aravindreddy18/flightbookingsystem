from django.db import models

# Create your models here.
class flight(models.Model):
    flightname = models.CharField(max_length=50)
    flightnumber = models.IntegerField()
    flightcapacity = models.IntegerField()
    flightclass = models.CharField(max_length=50)

    def __str__(self):
        return self.flightname