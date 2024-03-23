# Django
from django.db import models
from django.core.exceptions import ValidationError


class ActiveValidator():
    """Active validator.
    Esta clase actua como validador de registros activos.
    """

    def __call__(self, value):
        """Valida que el registro esté activo."""
        if isinstance(value, models.Model):
            if not value.is_active:
                raise ValidationError("El registro no está activo.")
        else:
            # El valor no es un modelo de Django, por lo que no se valida
            pass

    def deconstruct(self):
        return 'apps.base.validators.ActiveValidator', (), {}
