# Django Rest Framework
from rest_framework import viewsets, mixins

# Models
from apps.employee.models import Doctor

# Serializers
from apps.employee.serializers import DoctorSerializer


class DoctorViewSet(mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    queryset = Doctor.objects.filter(is_active=True)
    serializer_class = DoctorSerializer
