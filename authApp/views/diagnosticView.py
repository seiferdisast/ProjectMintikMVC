""" from rest_framework import generics
from authApp.models.diagnostic import Diagnostic
from authApp.serializers.diagnosticSerializer import DiagnosticSerializer, DiagnosticLiteSerializer

class DiagnosticListView(generics.ListAPIView):
    queryset = Diagnostic.objects.all()
    serializer_class = DiagnosticSerializer
   

class DiagnosticCreateView(generics.CreateAPIView):
    queryset = Diagnostic.objects.all()
    serializer_class = DiagnosticLiteSerializer
    """