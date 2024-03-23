# Django
from django.db import transaction

# DjangoRestFramework
from rest_framework import viewsets, status, mixins
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.decorators import action

# Spectacular
from drf_spectacular.utils import extend_schema

# Serializers
from apps.users.serializers.user_serializers import UserWithPasswordSerializer, UpdatePasswordSerializer
from apps.users.serializers.user_serializers import ListUserSerializer, UserSerializer
from apps.users.serializers.user_serializers import UserDoctorSerializer
from apps.employee.serializers import EmployeeSerializer, DoctorSerializer, PatientSerializer


class UserViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    list_serializer_class = ListUserSerializer
    serializer_class = UserSerializer
    parser_classes = [JSONParser, MultiPartParser]

    def get_queryset(self, pk=None):
        if pk is None:
            return self.list_serializer_class.Meta.model.objects.filter(is_active=True)
        return self.get_serializer().Meta.model.objects.filter(id=pk, is_active=True).first()

    @extend_schema(request=UserWithPasswordSerializer)
    def create(self, request, *args, **kwargs):
        """Crea un nuevo usuario."""
        serializer = UserWithPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(self.serializer_class(user).data, status=status.HTTP_201_CREATED)

    @extend_schema(responses={status.HTTP_200_OK: ListUserSerializer})
    def list(self, request, *args, **kwargs):
        """Lista todos los usuarios."""
        return super().list(request)

    def destroy(self, request, *args, **kwargs):
        """Elimina un usuario actualizando el campo is_active a False."""
        user = self.get_object()
        user.is_active = False
        user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @extend_schema(request=UpdatePasswordSerializer, responses={status.HTTP_200_OK: None})
    @action(detail=True, methods=["put"], url_path="update-password")
    def update_password(self, request, pk=None):
        """Actualiza la contraseña del usuario autenticado."""
        user = self.get_object()
        serializer = UpdatePasswordSerializer(data=request.data, context={"email": user.email})
        serializer.is_valid(raise_exception=True)
        user.set_password(serializer.validated_data["new_password"])
        user.save()
        return Response(status=status.HTTP_200_OK)

    @extend_schema(request=UserDoctorSerializer, responses={status.HTTP_200_OK: UserDoctorSerializer})
    @action(detail=False, methods=["post"], url_path="create-doctor")
    @transaction.atomic
    def create_doctor(self, request):
        """Crea un nuevo doctor."""
        user_data = {
            "email": request.data.pop("email"),
            "password": request.data.get("curp"),
            "confirm_password": request.data.get("curp"),
        }
        professional_id = request.data.pop("professional_id")

        curp = request.data.get("curp")
        employee = EmployeeSerializer.Meta.model.objects.filter(curp=curp).first()
        if employee is None:
            print("employee is None")
            employee_serializer = EmployeeSerializer(data=request.data)
            employee_serializer.is_valid(raise_exception=True)
            employee = employee_serializer.save()

        user_serializer = UserWithPasswordSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()
        doctor_data = {
            "professional_id": professional_id,
            "curp": employee.curp,
            "user": user.id,
        }
        doctor_serializer = DoctorSerializer(data=doctor_data)
        doctor_serializer.is_valid(raise_exception=True)
        doctor = doctor_serializer.save()

        return Response(status=status.HTTP_201_CREATED)
