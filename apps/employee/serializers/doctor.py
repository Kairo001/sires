# Rest Framework
from rest_framework import serializers

# Models
from apps.employee.models import Doctor


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        exclude = ("is_active",)
