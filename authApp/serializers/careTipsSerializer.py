from authApp.models.caretips import Caretips
from rest_framework import serializers

class CareTipsSerializer(serializers.ModelSerializer):
    class Mera:
        model = CareTyps
        fiels = ['careTip', 'careTipdate']