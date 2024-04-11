# DjangoRestFramework
from rest_framework.routers import DefaultRouter

# Views
from apps.employee.views import EmployeeViewSet, PatientViewSet, DoctorViewSet

router = DefaultRouter()

router.register(r"employees", EmployeeViewSet, basename="employees")
router.register(r"patients", PatientViewSet, basename="patients")
router.register(r"doctors", DoctorViewSet, basename="doctors")

urlpatterns = router.urls
