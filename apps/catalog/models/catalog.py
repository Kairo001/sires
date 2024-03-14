# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Base model
from apps.base.models import BaseModel


class CatalogType(BaseModel):
    """CatalogType model.
    Este modelo almacena los tipos de catálogos que se utilizarán en el sistema. Ejemplo: Estados, Genéros, etc.
    """
    id = models.AutoField(primary_key=True)
    value = models.CharField(
        _("Value"),
        max_length=50,
        unique=True,
        help_text=_("Valor del tipo de catálogo. Ejemplo: Estado, Género, etc."),
    )
    description = models.TextField(_("description"), null=True, blank=True)

    class Meta:
        db_table = "catalog_type"
        verbose_name = "Tipo de Catálogo"
        verbose_name_plural = "Tipos de Catálogos"

    def __str__(self):
        return self.value


class Catalog(BaseModel):
    """Catalog model.
    Este modelo almacena los catálogos que se utilizarán en el sistema. Ejemplo: Estados, Genéros, etc.
    """
    id = models.AutoField(primary_key=True)
    type = models.ForeignKey(CatalogType, on_delete=models.CASCADE, related_name="catalogs")
    code = models.CharField(
        _("Code"),
        max_length=30,
        null=True,
        blank=True,
        help_text=_("Código del catálogo. Ejemplo: MX, F, etc."),
    )
    value = models.CharField(
        _("value"),
        max_length=255,
        help_text=_("Valor del catálogo. Ejemplo: México, Femenino, etc."),
    )
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        related_name="children",
        null=True, blank=True,
        help_text=_("Catálogo padre. Ejemplo: México -> América, Morelia -> Michoacán, etc."),
    )
    description = models.TextField(_("description"), null=True, blank=True)

    class Meta:
        db_table = "catalog"
        verbose_name = "Catálogo"
        verbose_name_plural = "Catálogos"

    def __str__(self):
        return self.value

