from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ActivitiesView

router = DefaultRouter()
router.register(r"", ActivitiesView, basename="activity")

urlpatterns = [
    path("", include(router.urls)),
]
