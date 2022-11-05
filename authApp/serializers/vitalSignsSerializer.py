from authApp.models.vitalSigns import VitalSigns
from rest_framework import serializers

class VitalSignsSerializer(serializers.ModelSerializer):

    class Meta:
        model = VitalSigns
        fields = ['oximetry', 'respiratoryRate', 'heartRate', 'teperature', 'diastolicBloodPressure', 'systolicBloodPressure', 'blootGlucose']