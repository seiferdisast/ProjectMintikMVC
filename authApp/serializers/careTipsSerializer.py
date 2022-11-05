from authApp.models.careTips import CareTips
from rest_framework import serializers

class CareTipsSerializer(serializers.ModelSerializer):

    class Meta:
        model = CareTips
        fields = ['careTip']