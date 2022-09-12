from django.db import models 
from .user import user

class Diagnostic(models.Model):
 diagnosticID = models.Intfield('diagnosticID',primary_key = True)
 diagnostic = models.CharField(max_length=255)
 date = models.DateTimeField()
 users_documentID = models.Charfield('users_documentID',foreing_key = True)