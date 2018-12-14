from django.db import models
from geopy.distance import distance
from geopy.geocoders import Nominatim

class Job(models.Model):
	title = models.CharField(max_length=128)
	salary = models.IntegerField()
	location = models.CharField(max_length=512)
