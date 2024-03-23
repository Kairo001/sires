# Generated by Django 5.0.3 on 2024-03-20 02:16

import apps.base.validators
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Company",
            fields=[
                ("is_active", models.BooleanField(default=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "rfc",
                    models.CharField(
                        help_text="Registro Federal de Contribuyentes.",
                        max_length=13,
                        unique=True,
                        verbose_name="RFC",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Nombre de la empresa.",
                        max_length=100,
                        verbose_name="Name",
                    ),
                ),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="Description"),
                ),
            ],
            options={
                "verbose_name": "Empresa",
                "verbose_name_plural": "Empresas",
                "db_table": "company",
            },
        ),
        migrations.CreateModel(
            name="Employee",
            fields=[
                ("is_active", models.BooleanField(default=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "curp",
                    models.CharField(
                        help_text="Clave Única de Registro de Población.",
                        max_length=18,
                        primary_key=True,
                        serialize=False,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="La CURP no es válida.",
                                regex="^[A-Z]{4}[0-9]{6}[HM][A-Z]{5}[0-9]{2}$",
                            )
                        ],
                        verbose_name="CURP",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Nombre del empleado.",
                        max_length=100,
                        verbose_name="Name",
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        help_text="Apellido del empleado.",
                        max_length=100,
                        verbose_name="Last Name",
                    ),
                ),
                (
                    "second_last_name",
                    models.CharField(
                        blank=True,
                        help_text="Segundo apellido del empleado.",
                        max_length=100,
                        null=True,
                        verbose_name="Second Last Name",
                    ),
                ),
                (
                    "birth_date",
                    models.DateField(
                        help_text="Fecha de nacimiento del empleado.",
                        verbose_name="Birth Date",
                    ),
                ),
                (
                    "height",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        help_text="Altura del empleado.",
                        max_digits=3,
                        null=True,
                        verbose_name="Height",
                    ),
                ),
                (
                    "address",
                    models.TextField(
                        blank=True,
                        help_text="Dirección del empleado.",
                        null=True,
                        verbose_name="Address",
                    ),
                ),
                (
                    "mobile_phone",
                    models.CharField(
                        blank=True,
                        help_text="Número de teléfono móvil del empleado.",
                        max_length=10,
                        null=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="El número de teléfono móvil no es válido.",
                                regex="^[0-9]{10}$",
                            )
                        ],
                        verbose_name="Mobile Phone",
                    ),
                ),
                (
                    "social_security_number",
                    models.CharField(
                        blank=True,
                        help_text="Número de seguro social.",
                        max_length=11,
                        null=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="El número de seguro social no es válido.",
                                regex="^[0-9]{11}$",
                            )
                        ],
                        verbose_name="Social Security Number",
                    ),
                ),
                (
                    "postal_code",
                    models.CharField(
                        help_text="Código postal del empleado.",
                        max_length=5,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="El código postal debe contener 5 dígitos.",
                                regex="^[0-9]{5}$",
                            )
                        ],
                        verbose_name="Postal Code",
                    ),
                ),
                (
                    "academic_background",
                    models.ForeignKey(
                        help_text="Formación académica del empleado.",
                        limit_choices_to={"type__value": "Formación académica"},
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="employees_by_academic_background",
                        to="catalog.catalog",
                        validators=[apps.base.validators.ActiveValidator()],
                    ),
                ),
                (
                    "blood_type",
                    models.ForeignKey(
                        help_text="Tipo de sangre",
                        limit_choices_to={"type__value": "Tipo de sangre"},
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="employees_by_blood_type",
                        to="catalog.catalog",
                        validators=[apps.base.validators.ActiveValidator()],
                    ),
                ),
                (
                    "clues",
                    models.ForeignKey(
                        help_text="Catálogo de Clave Única de Establecimiento de Salud",
                        limit_choices_to={"type__value": "Clues"},
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="employees_by_clues",
                        to="catalog.catalog",
                        validators=[apps.base.validators.ActiveValidator()],
                    ),
                ),
                (
                    "company",
                    models.ForeignKey(
                        help_text="Empresa a la que pertenece el empleado.",
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="employees",
                        to="employee.company",
                        validators=[apps.base.validators.ActiveValidator()],
                    ),
                ),
                (
                    "federative_entity",
                    models.ForeignKey(
                        help_text="Entidad federativa del empleado.",
                        limit_choices_to={"type__value": "Entidad federativa"},
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="employees_by_federative_entity",
                        to="catalog.catalog",
                        validators=[apps.base.validators.ActiveValidator()],
                    ),
                ),
                (
                    "indigenous_language",
                    models.ForeignKey(
                        help_text="Lengua indígena del empleado.",
                        limit_choices_to={"type__value": "Lengua indígena"},
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="employees_by_indigenous_language",
                        to="catalog.catalog",
                        validators=[apps.base.validators.ActiveValidator()],
                    ),
                ),
                (
                    "locality",
                    models.ForeignKey(
                        help_text="Localidad del empleado.",
                        limit_choices_to={"type__value": "Localidad"},
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="employees_by_locality",
                        to="catalog.catalog",
                        validators=[apps.base.validators.ActiveValidator()],
                    ),
                ),
                (
                    "marital_status",
                    models.ForeignKey(
                        blank=True,
                        help_text="Estado civil del empleado.",
                        limit_choices_to={"type__value": "Estado Civil"},
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="employees_by_marital_status",
                        to="catalog.catalog",
                        validators=[apps.base.validators.ActiveValidator()],
                    ),
                ),
                (
                    "municipality",
                    models.ForeignKey(
                        help_text="Municipio del empleado.",
                        limit_choices_to={"type__value": "Municipio"},
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="employees_by_municipality",
                        to="catalog.catalog",
                        validators=[apps.base.validators.ActiveValidator()],
                    ),
                ),
                (
                    "nationality",
                    models.ForeignKey(
                        help_text="Nacionalidad del empleado.",
                        limit_choices_to={"type__value": "Nacionalidad"},
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="employees_by_nationality",
                        to="catalog.catalog",
                        validators=[apps.base.validators.ActiveValidator()],
                    ),
                ),
                (
                    "religion",
                    models.ForeignKey(
                        help_text="Religión del empleado.",
                        limit_choices_to={"type__value": "Religión"},
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="employees_by_religion",
                        to="catalog.catalog",
                        validators=[apps.base.validators.ActiveValidator()],
                    ),
                ),
                (
                    "sex",
                    models.ForeignKey(
                        help_text="Sexo del empleado.",
                        limit_choices_to={"type__value": "Sexo"},
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="employees_by_sex",
                        to="catalog.catalog",
                        validators=[apps.base.validators.ActiveValidator()],
                    ),
                ),
                (
                    "state_of_birth",
                    models.ForeignKey(
                        blank=True,
                        help_text="Estado de nacimiento del empleado.",
                        limit_choices_to={"type__value": "Entidad federativa"},
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="employees_by_state_of_birth",
                        to="catalog.catalog",
                        validators=[apps.base.validators.ActiveValidator()],
                    ),
                ),
            ],
            options={
                "verbose_name": "Empleado",
                "verbose_name_plural": "Empleados",
                "db_table": "employee",
            },
        ),
        migrations.CreateModel(
            name="Doctor",
            fields=[
                ("is_active", models.BooleanField(default=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "curp",
                    models.OneToOneField(
                        help_text="Clave Única de Registro de Población.",
                        on_delete=django.db.models.deletion.PROTECT,
                        primary_key=True,
                        related_name="doctor",
                        serialize=False,
                        to="employee.employee",
                    ),
                ),
                (
                    "professional_id",
                    models.CharField(
                        help_text="Número de cédula profesional.",
                        max_length=10,
                        unique=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="El número de cédula profesional no es válido.",
                                regex="^[0-9]{7}$",
                            )
                        ],
                        verbose_name="Professional ID",
                    ),
                ),
            ],
            options={
                "verbose_name": "Doctor",
                "verbose_name_plural": "Doctores",
                "db_table": "doctor",
            },
        ),
        migrations.CreateModel(
            name="Patient",
            fields=[
                ("is_active", models.BooleanField(default=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "curp",
                    models.OneToOneField(
                        help_text="Clave Única de Registro de Población.",
                        on_delete=django.db.models.deletion.PROTECT,
                        primary_key=True,
                        related_name="patient",
                        serialize=False,
                        to="employee.employee",
                    ),
                ),
            ],
            options={
                "verbose_name": "Paciente",
                "verbose_name_plural": "Pacientes",
                "db_table": "patient",
            },
        ),
    ]
