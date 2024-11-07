from django.db.models import PositiveSmallIntegerField, CharField
from django.core.validators import MaxValueValidator, MinValueValidator

from core.constants import ModelConstants


class BreedAttributeField(PositiveSmallIntegerField):
    """
    Кастомное поле, наследованное от PositiveSmallIntegerField.

    При инициализации поля ему автоматически присваиваются
    предопределенные значения choices, а также валидаторы для этого поля.
    Помимо этого, также указывается и help_text, при наличии
    указанного поля verbose_name при инициализации поля.

    Используется в модели Breed для упрощения кода и выноса повторяющихся
    значений в одно место.
    """

    def __init__(self, *args, **kwargs):
        """Инициализация экземпляра класса."""
        kwargs["choices"] = ModelConstants.ATTRIBUTE_CHOICES
        kwargs["validators"] = [MinValueValidator(1), MaxValueValidator(5)]
        super().__init__(*args, **kwargs)
        self.help_text = (
            f"{self.verbose_name}, от 1 до 5." if self.verbose_name else None
        )


class DogCharFieldAttributeField(CharField):
    """
    Кастомное поле, наследованное от CharField.

    При инициализации поля ему автоматически присваивается
    предопределенное значение max_length.

    Используется в модели Dog для упрощения кода и выноса повторяющихся
    значений в одно место.
    """

    def __init__(self, *args, **kwargs):
        """Инициализация экземпляра класса."""
        kwargs["max_length"] = ModelConstants.CHARFIELD_MAX_LENGTH
        super().__init__(*args, **kwargs)
