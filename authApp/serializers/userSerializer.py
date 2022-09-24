from rest_framework import serializers
from authApp.models.user  import User
from authApp.models.careTips import CareTips
from authApp.models.diagnostic import Diagnostic
from authApp.models.vitalSigns import VitalSigns

from authApp.serializers.careTipsSerializer import CareTipsSerializer
from authApp.serializers.diagnosticSerializer import DiagnosticSerializer
from authApp.serializers.vitalSignsSerializer import VitalSignsSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['documentId', 'name', 'lastName', 'cellularPhone', 'address', 'email', 'role', 'assignDoctor', 'assignNurse', 'assignRelative']

    def create(self, validated_data):
        userInstance = User.objects.create(**validated_data)
        return userInstance

    def to_representation(self, obj):
        user = User.objects.get(id=obj.documentId)
        return {
            'id': user.documentId,
            'username': user.name,
            'lastname': user.lastName,
            'cellullarPhone': user.cellularPhone,
            'address': user.address,
            'name': user.name,
            'email': user.email,
            'role': user.role,
            'assignDoctor' : UserSerializer(read_only=True),
            'assignNurse' : UserSerializer(read_only=True),
            'assignRelative' : UserSerializer(read_only=True)
    }