# Django
from django.db import models


class BaseModel(models.Model):
    """Base model.
    Esta clase actua como base abstracta de la que heredarán todos los demás modelos del proyecto.
    """
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        get_latest_by = "created"
        ordering = ["-created", "-updated"]
