# Rest Framework
from rest_framework import serializers

# Models
from apps.employee.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        exclude = ("is_active",)
