# Django Rest Framework
from rest_framework import viewsets

# Models
from apps.employee.models import Patient

# Serializers
from apps.employee.serializers import PatientSerializer


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.filter(is_active=True)
    serializer_class = PatientSerializer
