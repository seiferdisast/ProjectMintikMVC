from xml.dom.minidom import Document
from django.db import models
from .user import documentId

class caretips(models.Model):
    careTipsId: models.IntegerField(primary_key=True)
    careTip: models.CharField(255)
    dateTime: models.DateField
    users_documentID: models.ForeignKey( documentId, related_name='document', on_delete=models.CASCADE)
