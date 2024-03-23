# Rest Framework
from rest_framework import serializers

# Models
from apps.employee.models import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        exclude = ("is_active",)

