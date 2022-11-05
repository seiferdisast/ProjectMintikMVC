from authApp.models.diagnostic import Diagnostic
from rest_framework import serializers

class DiagnosticSerializer(serializers.ModelSerializer):

    class Meta:
        model = Diagnostic
        fields = ['patientDiagnostic']
