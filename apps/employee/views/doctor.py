# Django Rest Framework
from rest_framework import viewsets

# Models
from apps.employee.models import Doctor

# Serializers
from apps.employee.serializers import DoctorSerializer


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.filter(is_active=True)
    serializer_class = DoctorSerializer
