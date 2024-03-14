# DjangoRestFramework
from rest_framework.routers import DefaultRouter
from apps.catalog.views.catalog import CatalogViewSet, CatalogTypeViewSet

router = DefaultRouter()

router.register(r"catalogs", CatalogViewSet, basename="catalogs")
router.register(r"catalog-types", CatalogTypeViewSet, basename="catalog-types")

urlpatterns = router.urls
