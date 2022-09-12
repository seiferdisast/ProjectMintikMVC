from .user import User
from django.db import models

class medicalHistory(models.Model):
    oximetry = models.FloatField(default = 99)
    respiratoryRate = models.FloatField(default = 99)
    heartRate = models.FloatField(default = 99)
    temperature = models.FloatField(default = 49)
    diastolicBloodPressure = models.FloatField(default = 199)
    systolicBloodPressure = models.FloatField(default = 199)
    bloodGlucose = models.FloatField(default = 299)
    date = models.DateField