from django.db import models

# Create your models here.
class user_reg(models.Model):
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=300)
    email = models.CharField(max_length=200)
    mobile =models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    userid = models.CharField(max_length=200)
    password = models.CharField(max_length=200)


class user_complaints(models.Model):
    id = models.AutoField(primary_key=True)
    userid = models.CharField(max_length=300)
    username = models.CharField(max_length=200)
    email =models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    area_code = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    complaint_type = models.CharField(max_length=200)
    complaint = models.CharField(max_length=200)
    complaint_status = models.CharField(max_length=200)

