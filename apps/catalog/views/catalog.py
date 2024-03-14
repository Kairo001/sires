# DjangoRestFramework
from rest_framework import viewsets
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from django.shortcuts import get_object_or_404

# Serializers
from apps.catalog.serializers.catalog import CatalogTypeSerializer, CatalogSerializer

# Spectacular
from drf_spectacular.utils import extend_schema


class CatalogTypeViewSet(viewsets.ModelViewSet):
    serializer_class = CatalogTypeSerializer
    parser_classes = [JSONParser, MultiPartParser]

    def get_queryset(self, pk=None):
        if pk is None:
            return self.serializer_class.Meta.model.objects.filter(is_active=True)
        return self.get_serializer().Meta.model.objects.filter(id=pk, is_active=True).first()

    def destroy(self, request, *args, **kwargs):
        """Elimina un tipo de catálogo actualizando el campo is_active a False."""
        catalog_type = self.get_object()
        catalog_type.is_active = False
        catalog_type.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

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
    serializer_class = CatalogSerializer
    parser_classes = [JSONParser, MultiPartParser]

    def get_queryset(self, pk=None):
        if pk is None:
            return self.serializer_class.Meta.model.objects.filter(type__is_active=True, is_active=True)
        return self.get_serializer().Meta.model.objects.filter(id=pk, type__is_active=True, is_active=True).first()

    def destroy(self, request, *args, **kwargs):
        """Elimina un catálogo actualizando el campo is_active a False."""
        catalog = self.get_object()
        catalog.is_active = False
        catalog.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

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
