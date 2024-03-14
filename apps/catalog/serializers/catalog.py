# Rest Framework
from rest_framework import serializers

# Models
from apps.catalog.models import Catalog, CatalogType


class CatalogTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogType
        exclude = ("is_active",)


class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        exclude = ("is_active",)
