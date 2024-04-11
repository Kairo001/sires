# Django
from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

# Base model
from apps.base.models import BaseModel
from apps.base.validators import ActiveValidator

# Models
from apps.catalog.models import Catalog


class Employee(BaseModel):
    """employee model.
    Este modelo almacena la información de todos los empleados de una empresa.
    """
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name=_("ID"))
    curp = models.CharField(
        _("CURP"),
        unique=True,
        max_length=18,
        validators=[
            RegexValidator(
                regex=r"^[A-Z]{4}[0-9]{6}[HM][A-Z]{5}[0-9]{2}$",
                message=_("La CURP no es válida."),
            )
        ],
        help_text=_("Clave Única de Registro de Población."),
    )
    name = models.CharField(_("Name"), max_length=100, help_text=_("Nombre del empleado."))
    last_name = models.CharField(_("Last Name"), max_length=100, help_text=_("Apellido del empleado."))
    second_last_name = models.CharField(
        _("Second Last Name"),
        max_length=100,
        null=True, blank=True,
        help_text=_("Segundo apellido del empleado."),
    )
    birth_date = models.DateField(_("Birth Date"), help_text=_("Fecha de nacimiento del empleado."))
    height = models.DecimalField(
        _("Height"),
        max_digits=3,
        decimal_places=2,
        help_text=_("Altura del empleado."),
        null=True, blank=True,
    )
    address = models.TextField(_("Address"), help_text=_("Dirección del empleado."), null=True, blank=True)
    mobile_phone = models.CharField(
        _("Mobile Phone"),
        max_length=10,
        validators=[
            RegexValidator(
                regex=r"^[0-9]{10}$",
                message=_("El número de teléfono móvil no es válido."),
            )
        ],
        help_text=_("Número de teléfono móvil del empleado."),
        null=True, blank=True,
    )
    social_security_number = models.CharField(
        _("Social Security Number"),
        max_length=11,
        validators=[
            RegexValidator(
                regex=r"^[0-9]{11}$",
                message=_("El número de seguro social no es válido."),
            )
        ],
        help_text=_("Número de seguro social."),
        null=True, blank=True,
    )
    postal_code = models.CharField(
        _("Postal Code"),
        max_length=5,
        validators=[
            RegexValidator(
                regex="^[0-9]{5}$",
                message="El código postal debe contener 5 dígitos."
            )
        ],
        help_text=_("Código postal del empleado.")
    )
    sex = models.ForeignKey(
        Catalog,
        on_delete=models.PROTECT,
        related_name="employees_by_sex",
        validators=[ActiveValidator()],
        limit_choices_to={"type__value": "Sexo"},
        help_text=_("Sexo del empleado."),
    )
    blood_type = models.ForeignKey(
        Catalog,
        on_delete=models.PROTECT,
        related_name="employees_by_blood_type",
        validators=[ActiveValidator()],
        limit_choices_to={"type__value": "Tipo de sangre"},
        help_text=_("Tipo de sangre")
    )
    clues = models.ForeignKey(
        Catalog,
        on_delete=models.PROTECT,
        related_name="employees_by_clues",
        validators=[ActiveValidator()],
        limit_choices_to={"type__value": "Clues"},
        help_text=_("Catálogo de Clave Única de Establecimiento de Salud")
    )
    nationality = models.ForeignKey(
        Catalog,
        on_delete=models.PROTECT,
        related_name="employees_by_nationality",
        validators=[ActiveValidator()],
        limit_choices_to={"type__value": "Nacionalidad"},
        help_text=_("Nacionalidad del empleado.")
    )
    state_of_birth = models.ForeignKey(
        Catalog,
        on_delete=models.PROTECT,
        related_name="employees_by_state_of_birth",
        validators=[ActiveValidator()],
        limit_choices_to={"type__value": "Entidad federativa"},
        help_text=_("Estado de nacimiento del empleado."),
        null=True, blank=True,
    )
    religion = models.ForeignKey(
        Catalog,
        on_delete=models.PROTECT,
        related_name="employees_by_religion",
        validators=[ActiveValidator()],
        limit_choices_to={"type__value": "Religión"},
        help_text=_("Religión del empleado.")
    )
    marital_status = models.ForeignKey(
        Catalog,
        on_delete=models.PROTECT,
        related_name="employees_by_marital_status",
        validators=[ActiveValidator()],
        limit_choices_to={"type__value": "Estado Civil"},
        help_text=_("Estado civil del empleado."),
        null=True, blank=True
    )
    indigenous_language = models.ForeignKey(
        Catalog,
        on_delete=models.PROTECT,
        related_name="employees_by_indigenous_language",
        validators=[ActiveValidator()],
        limit_choices_to={"type__value": "Lengua indígena"},
        help_text=_("Lengua indígena del empleado.")
    )
    locality = models.ForeignKey(
        Catalog,
        on_delete=models.PROTECT,
        related_name="employees_by_locality",
        validators=[ActiveValidator()],
        limit_choices_to={"type__value": "Localidad"},
        help_text=_("Localidad del empleado.")
    )
    municipality = models.ForeignKey(
        Catalog,
        on_delete=models.PROTECT,
        related_name="employees_by_municipality",
        validators=[ActiveValidator()],
        limit_choices_to={"type__value": "Municipio"},
        help_text=_("Municipio del empleado.")
    )
    federative_entity = models.ForeignKey(
        Catalog,
        on_delete=models.PROTECT,
        related_name="employees_by_federative_entity",
        validators=[ActiveValidator()],
        limit_choices_to={"type__value": "Entidad federativa"},
        help_text=_("Entidad federativa del empleado.")
    )
    academic_background = models.ForeignKey(
        Catalog,
        on_delete=models.PROTECT,
        related_name="employees_by_academic_background",
        validators=[ActiveValidator()],
        limit_choices_to={"type__value": "Formación académica"},
        help_text=_("Formación académica del empleado.")
    )

    class Meta:
        db_table = "employee"
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
        indexes = [
            models.Index(fields=["curp"], name="employee_curp_idx"),
            models.Index(fields=["name"], name="employee_name_idx"),
            models.Index(fields=["last_name"], name="employee_last_name_idx"),
            models.Index(fields=["mobile_phone"], name="employee_mobile_phone_idx"),
        ]

    def __str__(self):
        return self.name

    def get_full_name(self):
        return f"{self.name} {self.last_name} {self.second_last_name}"
