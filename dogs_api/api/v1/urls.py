from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.v1.dogs.views import BreedViewSet, DogViewSet

v1_router = DefaultRouter()

v1_router.register("dogs", DogViewSet, basename="dogs")

v1_router.register("breeds", BreedViewSet, basename="breeds")

urlpatterns = [
    path("", include(v1_router.urls)),
]
