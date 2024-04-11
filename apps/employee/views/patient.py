# Django Rest Framework
from rest_framework import viewsets, mixins

# Models
from apps.employee.models import Patient

# Serializers
from apps.employee.serializers import PatientSerializer


class PatientViewSet(mixins.RetrieveModelMixin,
                     mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    queryset = Patient.objects.filter(is_active=True)
    serializer_class = PatientSerializer
