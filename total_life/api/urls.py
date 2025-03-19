from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClinicianViewSet, PatientViewSet, AppointmentViewSet

router = DefaultRouter()
router.register(r'clinicians', ClinicianViewSet)
router.register(r'patients', PatientViewSet)
router.register(r'appointments', AppointmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]