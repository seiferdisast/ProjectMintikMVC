from django.db import models
from .user import User

class CareTips(models.Model):
    careTipsId: models.AutoField(primary_key=True)
    careTip: models.CharField(max_length= 255)
    careTipdate: models.DateTimeField(auto_now=True)
    patient_documentID: models.ForeignKey(User, related_name='patientDocument3', on_delete=models.CASCADE)
 
 