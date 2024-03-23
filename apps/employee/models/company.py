# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Base model
from apps.base.models import BaseModel


class Company(BaseModel):
    """Company model.
    Este modelo almacena la información de las empresas que se registrarán en el sistema.
    """
    id = models.AutoField(primary_key=True)
    rfc = models.CharField(
        _("RFC"),
        max_length=13,
        unique=True,
        help_text=_("Registro Federal de Contribuyentes."),
    )
    name = models.CharField(_("Name"), max_length=100, help_text=_("Nombre de la empresa."))
    description = models.TextField(_("Description"), null=True, blank=True)

    class Meta:
        db_table = "company"
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"

    def __str__(self):
        return self.name
