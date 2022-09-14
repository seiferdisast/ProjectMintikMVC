from django.db import models
from .user import User

class VitalSigns(models.Model):
    vitalSignsID = models.IntegerField(default = 10)
    oximetry = models.FloatField(default = 99)
    respiratoryRate = models.FloatField(default = 99)
    heartRate = models.FloatField(default = 99)
    temperature = models.FloatField(default = 49)
    diastolicBloodPressure = models.FloatField(default = 199)
    systolicBloodPressure = models.FloatField(default = 199)
    bloodGlucose = models.FloatField(default = 299)
    vitalSignsDate = models.DateTimeField()
    patientDocumentId = models.ForeignKey(User, related_name='patient_document', on_delete=models.CASCADE)
