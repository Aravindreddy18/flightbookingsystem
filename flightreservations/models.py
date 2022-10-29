from django.db import models

# Create your models here.
class flight(models.Model):
    flightname = models.CharField(max_length=50)
    flightnumber = models.IntegerField()
    flightcapacity = models.IntegerField()
    flightclass = models.CharField(max_length=50)

    def __str__(self):
        return self.flightname

class reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=60)
    phone = models.IntegerField()
    passengercount = models.IntegerField()
    ticketprice = models.IntegerField()
    departuredate = models.DateField()
    arrivaldate = models.DateField()
    flightclass = models.CharField(max_length=50)


    def __str__(self):
        return self.name