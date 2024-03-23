# Rest Framework
from rest_framework import serializers

# Models
from apps.employee.models import Patient


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        exclude = ("is_active",)
