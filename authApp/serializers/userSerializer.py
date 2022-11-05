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

    def update(self, instance, validated_data):
        instance.documentId = validated_data.get('documentId', instance.documentId)
        instance.save()
        return instance

    def to_representation(self, obj):
        if(obj is None):
            return None

        user = User.objects.get(pk=obj.documentId)
        return {
            'documentId': user.documentId,
            'name': user.name,
            'lastname': user.lastName,
            'cellullarPhone': user.cellularPhone,
            'address': user.address,
            'email': user.email,
            'role': user.role,
            'assignDoctor' : UserSerializer().to_representation(user.assignDoctor), #if(user.assignDoctor is not None) else None,
            'assignNurse' : UserSerializer().to_representation(user.assignNurse),#if(user.assignNurse is not None) else None,
            'assignRelative' : UserSerializer().to_representation(user.assignRelative)#if(user.assignRelative is not None) else None
    }

class UserLiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['documentId']

class UserWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"