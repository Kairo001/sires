from collections import OrderedDict

# Rest Framework
from rest_framework import serializers

# Models
from apps.employee.models import Employee


class ListEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ("id", "curp", "name", "last_name", "second_last_name")


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        exclude = ("is_active",)

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret["sex"] = instance.sex.value
        ret["blood_type"] = instance.blood_type.value
        ret["clues"] = instance.clues.value
        ret["nationality"] = instance.nationality.value
        ret["state_of_birth"] = instance.state_of_birth.value
        ret["religion"] = instance.religion.value
        ret["marital_status"] = instance.marital_status.value
        ret["indigenous_language"] = instance.indigenous_language.value
        ret["locality"] = instance.locality.value
        ret["municipality"] = instance.municipality.value
        ret["federative_entity"] = instance.federative_entity.value
        ret["academic_background"] = instance.academic_background.value
        return ret
