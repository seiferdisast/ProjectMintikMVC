from rest_framework import serializers
from authApp.models.user  import User
from authApp.models.careTips import Caretips
from authApp.models.diagnostic import Diagnostic
from authApp.models.vitalSigns import VitalSigns
from authApp.serializers.careTipsSerializer import CareTipsSerializer
from authApp.serializers.diagnosticSerializer import DiagnosticSerializer
from authApp.serializers.vitalSignsSerializer import VitalSignsSerializer

class UserSerializer(serializers.ModelSerializer):
    #MI NO ENTENDER, ME VOY A DORMIR


('documentId', 'name', 'lastName', 'cellularPhone', 'address', 'email', 'role', 'password', 'assignDoctor', 'assignNurse', 'assignRelative', 'some_salt', 'objects', )