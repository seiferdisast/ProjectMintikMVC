from django.db import models
from .user import User

class vitalSigns(models.Model):
    vitalSignsID = models.IntegerField(default = 10)
    oximetry = models.FloatField(default = 99)
    respiratoryRate = models.FloatField(default = 99)
    heartRate = models.FloatField(default = 99)
    temperature = models.FloatField(default = 49)
    diastolicBloodPressure = models.FloatField(default = 199)
    systolicBloodPressure = models.FloatField(default = 199)
    bloodGlucose = models.FloatField(default = 299)
    date = models.DateField()
    userDocumentID = models.IntegerField(max_length = 10)
