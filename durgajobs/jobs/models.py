from django.db import models

# Create your models here.
class hydjobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    eligibility=models.CharField(max_length=50)
    address=models.TextField()
    email=models.EmailField()
    phonenumber=models.BigIntegerField()
class banglorejobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    eligibility=models.CharField(max_length=50)
    address=models.TextField()
    email=models.EmailField()
    phonenumber=models.BigIntegerField()
class punejobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    eligibility=models.CharField(max_length=50)
    address=models.TextField()
    email=models.EmailField()
    phonenumber=models.BigIntegerField()