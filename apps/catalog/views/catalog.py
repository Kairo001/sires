# DjangoRestFramework
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

# Serializers
from apps.catalog.serializers.catalog import CatalogTypeSerializer, CatalogSerializer

# Spectacular
from drf_spectacular.utils import extend_schema

# Filters
from django_filters import rest_framework as filters


class CatalogTypeViewSet(viewsets.ModelViewSet):
    queryset = CatalogTypeSerializer.Meta.model.objects.filter(is_active=True)
    serializer_class = CatalogTypeSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ["value"]

    @extend_schema(responses={status.HTTP_200_OK: CatalogSerializer(many=True)})
    @action(detail=True, methods=["get"])
    def catalogs(self, request, pk=None):
        """Lista todos los catálogos de un tipo de catálogo."""
        catalog_type = self.get_object()
        catalogs = catalog_type.catalogs.filter(is_active=True)

        page = self.paginate_queryset(catalogs)
        if page is not None:
            serializer = CatalogSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = CatalogSerializer(catalogs, many=True)
        return Response(serializer.data)


class CatalogViewSet(viewsets.ModelViewSet):
    queryset = CatalogSerializer.Meta.model.objects.filter(type__is_active=True, is_active=True)
    serializer_class = CatalogSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ["type__value", "value", "parent__value", "code"]

    @extend_schema(responses={status.HTTP_200_OK: CatalogSerializer(many=True)})
    @action(detail=True, methods=["get"])
    def children(self, request, pk=None):
        """Lista todos los catálogos hijos de un catálogo."""
        catalog = self.get_object()
        children = catalog.children.filter(is_active=True)

        page = self.paginate_queryset(children)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(children, many=True)
        return Response(serializer.data)
