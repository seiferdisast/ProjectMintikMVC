from django.db import models 
from .user import User

class Diagnostic(models.Model):
    diagnosticId = models.AutoField(primary_key = True)
    patientDiagnostic = models.CharField(max_length = 255)
    date = models.DateTimeField()
    patient_documentId = models.ForeignKey(User, related_name='patient_document1', on_delete=models.CASCADE)
