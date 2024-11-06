from django.db import models

from .constants import ModelConstants

class NameBaseModel(models.Model):
    """Абстрактная модель, включающая в себя повторяющееся поле name."""

    name = models.CharField(max_length=ModelConstants.CHARFIELD_MAX_LENGTH)

    class Meta:
        abstract = True
        default_related_name = "%(class)ss"
        ordering = ("id",)


    def __str__(self) -> str:
        """
        Переопределяем стандартный вывод метода __str__.

        Используется для более точного отображения данных об объекте модели.
        """
        return self.name[:ModelConstants.OFFSET_FOR_STR_METHOD]
