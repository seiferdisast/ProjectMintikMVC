from django.db import models
from .user import User

class CareTips(models.Model):
    careTipsId: models.AutoField(primary_key=True)
    careTip: models.CharField(max_length= 255)
    CareTipdate: models.DateTimeField()
    patientDocumentID: models.ForeignKey(User, related_name='patientDocumentID', on_delete=models.CASCADE)
 
 