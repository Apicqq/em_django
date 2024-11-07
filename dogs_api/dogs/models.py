from django.core.validators import MinValueValidator
from django.db import models

from core.constants import ModelConstants
from core.models import NameBaseModel
from core.extra_fields import BreedAttributeField, DogCharFieldAttributeField

class Dog(NameBaseModel):
    """Модель для хранения информации о собаках."""

    age = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1)],
    )
    breed = models.ForeignKey(
        "Breed",
        on_delete=models.CASCADE,
        verbose_name="Порода",
    )
    gender = DogCharFieldAttributeField("Пол")
    color = DogCharFieldAttributeField("Окрас")
    favorite_food = DogCharFieldAttributeField("Любимая еда")
    favorite_toy = DogCharFieldAttributeField("Любимая игрушка")

    class Meta:
        verbose_name = "Собака"
        verbose_name_plural = "Собаки"



class Breed(NameBaseModel):
    """Модель для хранения информации о породах собак."""

    class SizeChoices(models.TextChoices):
        """Enum для хранения размеров пород собак."""

        TINY = "Tiny", "Крошечный"
        SMALL = "Small", "Маленький"
        MEDIUM = "Medium", "Средний"
        LARGE = "Large", "Большой"

    size = models.CharField(
        max_length=ModelConstants.SIZE_CHOICES_MAX_LENGTH,
        choices=SizeChoices.choices,
        default=SizeChoices.MEDIUM,
    )
    friendliness = BreedAttributeField("Дружелюбность")
    trainability = BreedAttributeField("Обучаемость")
    shedding_amount = BreedAttributeField("Линючесть")
    exercise_needs = BreedAttributeField("Нужда в тренировках")

    class Meta:
        verbose_name = "Порода"
        verbose_name_plural = "Породы"
