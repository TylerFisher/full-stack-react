from django.urls import include, path
from rest_framework import routers

from .viewsets import (
    BodyViewSet,
    DivisionViewSet,
    DivisionLevelViewSet,
    OfficeViewSet,
    OfficeholderViewSet,
    PartyViewSet,
    PersonViewSet,
)

router = routers.DefaultRouter()

router.register(r"bodies", BodyViewSet)
router.register(r"divisions", DivisionViewSet)
router.register(r"division-levels", DivisionLevelViewSet)
router.register(r"offices", OfficeViewSet)
router.register(r"officeholders", OfficeholderViewSet)
router.register(r"parties", PartyViewSet)
router.register(r"people", PersonViewSet)


urlpatterns = [path("api/", include(router.urls))]
