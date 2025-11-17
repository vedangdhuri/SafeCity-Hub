from django.db import models

# Create your models here.
class criminal_details(models.Model):
    id = models.AutoField(primary_key=True)
    station_name = models.CharField(max_length=300)
    arae_code = models.CharField(max_length=200)
    city =models.CharField(max_length=200)
    criminal_name = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200)
    complaint_type = models.CharField(max_length=200)
    acts = models.CharField(max_length=200)
    sessions = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    criminal_image = models.FileField()