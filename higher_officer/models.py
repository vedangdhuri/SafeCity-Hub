from django.db import models

# Create your models here.
class station_details(models.Model):
    id = models.AutoField(primary_key=True)
    police_name = models.CharField(max_length=300)
    gender = models.CharField(max_length=300)
    station_name = models.CharField(max_length=300)
    area_code = models.CharField(max_length=200)
    location =models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    userid=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    area_name = models.CharField(max_length=200)
