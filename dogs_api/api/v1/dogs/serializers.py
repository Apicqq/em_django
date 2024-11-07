from rest_framework.serializers import ModelSerializer

from dogs.models import Breed, Dog


class BreedGetSerializer(ModelSerializer):
    """Сериализатор для GET-запросов модели Breed."""

    class Meta:
        model = Breed
        fields = (
            "id",
            "name",
            "size",
            "friendliness",
            "shedding_amount",
            "exercise_needs",
            "trainability",
        )


class BreedPostSerializer(ModelSerializer):
    """Сериализатор для POST-запросов модели Breed."""

    class Meta:
        model = Breed
        exclude = ("id",)


class DogGetSerializer(ModelSerializer):
    """Сериализатор для GET-запросов модели Dog."""

    class Meta:
        model = Dog
        fields = (
            "id",
            "name",
            "age",
            "breed",
            "gender",
            "color",
            "favorite_food",
            "favorite_toy",
        )


class DogPostSerializer(ModelSerializer):
    """Сериализатор для POST-запросов модели Dog."""

    class Meta:
        model = Dog
        exclude = ("id",)
