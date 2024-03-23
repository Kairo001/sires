# Django Rest Framework
from rest_framework import viewsets

# Models
from apps.employee.models import Company

# Serializers
from apps.employee.serializers import CompanySerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.filter(is_active=True)
    serializer_class = CompanySerializer
