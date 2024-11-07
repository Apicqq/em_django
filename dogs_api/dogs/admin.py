from django.contrib import admin

from dogs.models import Breed, Dog

class DogInLine(admin.StackedInline):
    """Inline класс для модели Dog."""

    model = Dog

@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    """Базовая админ-панель для модели Dog."""

    list_display = (
        "id",
        "age",
        "breed",
        "gender",
        "color",
        "favorite_food",
        "favorite_toy",
    )

@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    """Базовая админ-панель для модели Breed."""

    list_display = (
        "id",
        "size",
        "friendliness",
        "shedding_amount",
        "exercise_needs",
    )
    inlines = [DogInLine]
