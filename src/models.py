from django.db import models

# Create your models here.
from geopy.geocoders import Nominatim

class Shop(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    pincode = models.CharField(max_length=10)
    lat = models.CharField(max_length=20 , null=True , blank=True)
    lon = models.CharField(max_length=20 , null=True , blank=True)
    
    
    def save(self, *args, **kwargs):
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(int(self.pincode))
        self.lat = location.latitude
        self.lon = location.longitude
        super(Shop, self).save(*args, **kwargs)
            
    def __str__(self):
        return self.name

    