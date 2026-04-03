from django.db import models


class Event(models.Model):
    img  = models.ImageField(upload_to='pic')
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Booking(models.Model):
    cus_name     = models.CharField(max_length=100)
    cus_ph       = models.CharField(max_length=15)
    name         = models.ForeignKey(Event, on_delete=models.CASCADE)
    booking_date = models.DateField()
    booked_on    = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.cus_name} — {self.name} ({self.booking_date})'
