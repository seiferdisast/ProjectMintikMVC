from django.db import models 
from .user import user

class Diagnostic(models.Model):
 diagnosticID = models.IntegerField(default = 10)
 patient_diagnostic = models.CharField(default = 255)
 date = models.DateTimeField()
 users_documentID = models.CharField(default = 10)