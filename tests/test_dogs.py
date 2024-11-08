from http import HTTPStatus

from django.test import Client
import pytest

from dogs.models import Dog

DOGS_URL = "/api/v1/dogs/"


@pytest.mark.django_db
def test_get_dogs_list(dogs_list: list[Dog], client: Client) -> None:
    response = client.get(DOGS_URL)
    assert response.status_code == HTTPStatus.OK, (
        "Проверьте, что при GET-запросе по адресу "
        f"{DOGS_URL} возвращается список собак."
    )
    dogs_data = response.json()
    assert isinstance(dogs_data, dict), (
        f"Проверьте, что для эндпоинта {DOGS_URL}"
        f"список собак возвращается в виде словаря"
    )
    assert all(
        key in dogs_data for key in ("count", "next", "previous", "results")
    ), f"Проверьте, что для эндпоинта {DOGS_URL} настроена пагинация."
    assert len(dogs_data.get("results")) == Dog.objects.count(), (
        "Проверьте, что при GET-запросе пользователя возвращается "
        "весь список существующих собак."
    )


@pytest.mark.django_db
@pytest.mark.parametrize(
    "field",
    [
        "id",
        "name",
        "age",
        "breed",
        "gender",
        "color",
        "favorite_food",
        "favorite_toy",
    ],
)
def test_get_dog_detail(client: Client, dog: Dog, field: str) -> None:
    response = client.get(f"{DOGS_URL}{dog.id}/")
    assert response.status_code == HTTPStatus.OK, (
        "Проверьте, что при GET-запросе по адресу "
        f"{DOGS_URL}{dog.id} возвращается ответ со статусом {HTTPStatus.OK}."
    )
    dog_data = response.json()
    assert isinstance(dog_data, dict), (
        f"Проверьте, что при отправке запроса на эндпоинт"
        f" {DOGS_URL}{dog.id} возвращается словарь с данными о собаке"
    )
    assert field in dog_data, (
        "Проверьте, что при GET-запросе по адресу "
        f"{DOGS_URL}{dog.id} в ответе содержится поле {field}"
    )


@pytest.mark.django_db
def test_post_dog(client: Client, dog_payload: dict) -> None:
    response = client.post(DOGS_URL, data=dog_payload, format="json")
    assert response.status_code == HTTPStatus.CREATED, (
        "Проверьте, что при POST-запросе по адресу "
        f"{DOGS_URL} возвращается ответ со статусом {HTTPStatus.CREATED}."
    )
    dog_data = response.json()
    assert isinstance(dog_data, dict), (
        "Проверьте, что при корректном POST-запросе по адресу "
        f"{DOGS_URL} в ответе возвращается словарь с данными о собаке"
    )

    assert Dog.objects.count() == 1, (
        "Проверьте, что при корректном POST-запросе по адресу "
        f"{DOGS_URL} в базе данных создается новая запись о собаке"
    )


@pytest.mark.django_db
@pytest.mark.parametrize("invalid_data", [{"name": "Basya" * 100}])
def test_post_dog_invalid_data(
    client: Client,
    invalid_data: dict[str, [str | int]],
) -> None:
    response = client.post(DOGS_URL, data=invalid_data, format="json")
    assert response.status_code == HTTPStatus.BAD_REQUEST, (
        "Проверьте, что при POST-запросе по адресу "
        f"{DOGS_URL} возвращается ответ со статусом {HTTPStatus.BAD_REQUEST}."
    )
    assert not Dog.objects.count(), (
        "Проверьте, что при POST-запросе по адресу "
        f"{DOGS_URL} не создается новая запись о собаке"
    )


@pytest.mark.django_db
def test_delete_dog(client: Client, dog: Dog) -> None:
    response = client.delete(f"{DOGS_URL}{dog.id}/")
    assert response.status_code == HTTPStatus.NO_CONTENT, (
        "Проверьте, что при DELETE-запросе по адресу "
        f"{DOGS_URL}{dog.id} возвращается"
        f" ответ со статусом {HTTPStatus.NO_CONTENT}."
    )

    assert not Dog.objects.count(), (
        "Проверьте, что при DELETE-запросе по адресу "
        f"{DOGS_URL}{dog.id} удаляется запись о собаке"
    )
