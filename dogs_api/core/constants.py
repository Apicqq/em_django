"""Constants used for the project."""

from enum import Enum


class ModelConstants:
    """Константы, используемые для моделей."""

    CHARFIELD_MAX_LENGTH = 100
    ATTRIBUTE_CHOICES = [(i, i) for i in range(1, 6)]
    OFFSET_FOR_STR_METHOD = 30

    class SizeChoices(Enum):
        TINY = "t", "Крошечный"
        SMALL = "s", "Маленький"
        MEDIUM = "m", "Средний"
        LARGE = "l", "Большой"
