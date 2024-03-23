from django.contrib import admin
from apps.catalog.models import CatalogType, Catalog


class CatalogTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "value", "description")
    list_display_links = ("id",)
    search_fields = ("value",)
    list_filter = ("value",)


class CatalogAdmin(admin.ModelAdmin):
    list_display = ("id", "type", "code", "value", "parent", "description")
    list_display_links = ("id",)
    search_fields = ("value", "parent__value")
    list_filter = ("type", "value", "parent")


admin.site.register(CatalogType, CatalogTypeAdmin)
admin.site.register(Catalog, CatalogAdmin)
