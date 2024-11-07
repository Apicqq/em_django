from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import viewsets

from dogs.models import Dog, Breed
from api.v1.dogs.serializers import DogGetSerializer, BreedGetSerializer, \
    BreedPostSerializer, DogPostSerializer


@extend_schema_view(
    list=extend_schema(
        summary="Вернуть список всех собак.",
        description="Возвращает список всех собак.",
    ),
    retrieve=extend_schema(
        summary="Получить объект собаки по ID.",
        description="Возвращает конкретную собаку.",
    ),
    create=extend_schema(
        summary="Создать новую собаку.",
        description="Создает новую собаку.",
    ),
    update=extend_schema(
        summary="Полностью обновить объект собаки по ID.",
        description="Обновляет конкретную собаку.",
    ),
    destroy=extend_schema(
        summary="Удалить объект собаки по ID.",
        description="Удаляет конкретную собаку.",
    ),
)
class DogViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели Dog."""

    queryset = Dog.objects.select_related("breed")
    http_method_names = ("get", "post", "put", "delete")

    def get_serializer_class(self):
        """
        Метод для выбора сериализатора.

        Для GET-запросов используется сериализатор DogGetSerializer,
        для POST-запросов - DogPostSerializer.
        """
        if self.action in ("list", "retrieve"):
            return DogGetSerializer
        return DogPostSerializer


@extend_schema_view(
    list=extend_schema(
        summary="Вернуть список всех пород.",
        description="Возвращает список всех пород.",
    ),
    retrieve=extend_schema(
        summary="Получить объект породы по ID.",
        description="Возвращает конкретную породу.",
    ),
    create=extend_schema(
        summary="Создать новую породу.",
        description="Создает новую породу.",
    ),
    update=extend_schema(
        summary="Полностью обновить объект породы по ID.",
        description="Обновляет конкретную породу.",
    ),
    destroy=extend_schema(
        summary="Удалить объект породы по ID.",
        description="Удаляет конкретную породу.",
    ),
)
class BreedViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели Breed."""

    queryset = Breed.objects.all()
    http_method_names = ("get", "post", "put", "delete")

    def get_serializer_class(self):
        """
        Метод для выбора сериализатора.

        Для GET-запросов используется сериализатор BreedGetSerializer,
        для POST-запросов - BreedPostSerializer.
        """
        if self.action in ("list", "retrieve"):
            return BreedGetSerializer
        return BreedPostSerializer
