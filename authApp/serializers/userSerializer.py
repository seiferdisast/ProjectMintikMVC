from rest_framework import serializers
from authApp.models.user  import User
from authApp.models.careTips import CareTips
from authApp.models.diagnostic import Diagnostic
from authApp.models.vitalSigns import VitalSigns

from authApp.serializers.careTipsSerializer import CareTipsSerializer
from authApp.serializers.diagnosticSerializer import DiagnosticSerializer
from authApp.serializers.vitalSignsSerializer import VitalSignsSerializer


class UserSerializer(serializers.ModelSerializer):
    careTip = CareTipsSerializer()
    diagnostic = DiagnosticSerializer()
    vitalSign = VitalSignsSerializer()

    class Meta:
        model = User
        fields = ['documentId', 'name', 'lastName', 'cellularPhone', 'address', 'email', 'role', 'assignDoctor', 'assignNurse', 'assignRelative']

    def create(self, validated_data):
        careTipData = validated_data.pop('careTip')
        diagnosticData = validated_data.pop('diagnostic')
        vitalSignData = validated_data.pop('vitalSign')
        userInstance = User.objects.create(**validated_data)
        CareTips.objects.create(user=userInstance, **careTipDataData)
        Diagnostic.objects.create(user=userInstance, **diagnosticData)
        VitalSigns.objects.create(user=userInstance, **vitalSingnData)
        return userInstance

    def to_representation(self, obj):
        user = User.objects.get(id=obj.documentId)
        account = Account.objects.get(user=obj.documentId)
        return {
            'id': user.documentId,
            'username': user.name,
            'lastname': user.lastName,
            'cellullarPhone': user.cellularPhone,
            'address': user.address,
            'name': user.name,
            'email': user.email,
            'role': user.role,
            'assignDoctor' : {},
            'assignNurse' : null,
            'assignRelative' : null
    }