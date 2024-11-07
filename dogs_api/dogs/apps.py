from django.apps import AppConfig


class DogsConfig(AppConfig):
    """Класс-конфигуратор для приложения Dogs."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "dogs"
