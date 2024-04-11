# Django Rest Framework
from rest_framework import viewsets, mixins, status
from rest_framework.response import Response

# Models
from apps.employee.models import Employee

# Serializers
from apps.employee.serializers import EmployeeSerializer, ListEmployeeSerializer

# Filters
from django_filters import rest_framework as filters


class EmployeeFilter(filters.FilterSet):
    curp = filters.CharFilter(lookup_expr='contains')
    name = filters.CharFilter(lookup_expr='contains')
    last_name = filters.CharFilter(lookup_expr='contains')
    mobile_phone = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Employee
        fields = ['curp', 'name', 'last_name', 'mobile_phone']


class EmployeeViewSet(mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.ListModelMixin,
                      viewsets.GenericViewSet):
    list_serializer_class = ListEmployeeSerializer
    serializer_class = EmployeeSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = EmployeeFilter

    def get_queryset(self, pk=None):
        if pk is None:
            return self.list_serializer_class.Meta.model.objects.filter(is_active=True)
        return self.get_serializer().Meta.model.objects.filter(id=pk, is_active=True).first()

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
