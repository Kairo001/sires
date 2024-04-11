# Django
from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

# Base model
from apps.base.models import BaseModel

# Models
from apps.employee.models import Employee
from apps.users.models import User


class Doctor(BaseModel):
    """Doctor model.
    Este modelo almacena la información de los doctores que se registrarán en el sistema.
    El doctor es un empleado que tiene un número de cédula profesional.
    """
    employee = models.OneToOneField(
        Employee,
        on_delete=models.PROTECT,
        related_name="doctor",
        help_text=_("Clave Única de Registro de Población."),
    )
    professional_id = models.CharField(
        _("Professional ID"),
        max_length=8,
        unique=True,
        validators=[
            RegexValidator(
                regex=r"^[0-9]{8}$",
                message=_("El número de cédula profesional no es válido."),
            )
        ],
        help_text=_("Número de cédula profesional."),
    )
    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        related_name="doctor",
        help_text=_("Usuario asociado al doctor."),
    )

    class Meta:
        db_table = "doctor"
        verbose_name = "Doctor"
        verbose_name_plural = "Doctores"

    def __str__(self):
        return self.employee.name

    def get_full_name(self):
        return f"{self.employee.name} {self.employee.last_name} {self.employee.second_last_name}"
