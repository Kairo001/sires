# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Base model
from apps.base.models import BaseModel

# Models
from apps.employee.models import Employee
from apps.users.models import User


class Patient(BaseModel):
    """Patient model.
    Este modelo almacena la información de los pacientes que se registrarán en el sistema.
    El paciente es un empleado que tiene un número de seguro social.
    """
    employee = models.OneToOneField(
        Employee,
        on_delete=models.PROTECT,
        related_name="patient",
        help_text=_("Clave Única de Registro de Población."),
    )

    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        related_name="patient",
        help_text=_("Usuario asociado al paciente."),
    )

    class Meta:
        db_table = "patient"
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"

    def __str__(self):
        return self.employee.name

    def get_full_name(self):
        return f"{self.employee.name} {self.employee.last_name} {self.employee.second_last_name}"
