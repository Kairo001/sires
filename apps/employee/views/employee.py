# Django Rest Framework
from rest_framework import viewsets

# Models
from apps.employee.models import Employee

# Serializers
from apps.employee.serializers import EmployeeSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.filter(is_active=True)
    serializer_class = EmployeeSerializer
