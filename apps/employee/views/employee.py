# Django Rest Framework
from rest_framework import viewsets, mixins, status
from rest_framework.response import Response

# Models
from apps.employee.models import Employee

# Serializers
from apps.employee.serializers import EmployeeSerializer, ListEmployeeSerializer

# Filters
from django_filters import rest_framework as filters

# Spectacular
from drf_spectacular.utils import extend_schema


class EmployeeViewSet(mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.ListModelMixin,
                      viewsets.GenericViewSet):
    queryset = Employee.objects.filter(is_active=True)
    list_serializer_class = ListEmployeeSerializer
    serializer_class = EmployeeSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['curp', 'name', 'last_name', 'mobile_phone']

    @extend_schema(responses={status.HTTP_200_OK: ListEmployeeSerializer})
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.list_serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.list_serializer_class(queryset, many=True)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        instance.save()
        if hasattr(instance, 'doctor'):
            instance.doctor.is_active = False
            instance.doctor.save()
            instance.doctor.user.is_active = False
            instance.doctor.user.save()
        if hasattr(instance, 'patient'):
            instance.patient.is_active = False
            instance.patient.save()
            instance.patient.user.is_active = False
            instance.patient.user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
