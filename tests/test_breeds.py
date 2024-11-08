from http import HTTPStatus

from django.test import Client
import pytest

from dogs.models import Breed

BREEDS_URL = "/api/v1/breeds/"


@pytest.mark.django_db
def test_get_breeds_list(breed_list: list[Breed], client: Client) -> None:
    response = client.get(BREEDS_URL)
    assert response.status_code == HTTPStatus.OK, (
        "Проверьте, что при GET-запросе по адресу "
        f"{BREEDS_URL} возвращается список пород собак."
    )

    data = response.json()

    assert isinstance(data, dict), (
        f"Проверьте, что для эндпоинта {BREEDS_URL}"
        f"список пород возвращается в виде словаря"
    )

    assert all(
        key in data for key in ("count", "next", "previous", "results")
    ), f"Проверьте, что для эндпоинта {BREEDS_URL} настроена пагинация."
    assert len(data.get("results")) == Breed.objects.count(), (
        "Проверьте, что при GET-запросе пользователя возвращается "
        "весь список существующих пород."
    )


@pytest.mark.django_db
@pytest.mark.parametrize(
    "field",
    [
        "id",
        "name",
        "size",
        "friendliness",
        "trainability",
        "shedding_amount",
        "exercise_needs",
    ],
)
def test_get_breed_detail(client: Client, breed: Breed, field: str) -> None:
    response = client.get(f"{BREEDS_URL}{breed.id}/")

    assert response.status_code == HTTPStatus.OK, (
        "Проверьте, что при GET-запросе по адресу "
        f"{BREEDS_URL}{breed.id} возвращается порода собаки."
    )

    breed_data = response.json()

    assert isinstance(breed_data, dict), (
        f"Проверьте, что при отправке запроса на эндпоинт"
        f" {BREEDS_URL}{breed.id} возвращается словарь с данными о породе"
    )

    assert field in breed_data, (
        "Проверьте, что при GET-запросе по адресу"
        f"{BREEDS_URL}{breed.id} в словаре с данными о породе присутствует"
        f"поле {field}"
    )


@pytest.mark.django_db
def test_create_breed_valid_data(client: Client, breed_payload: dict):
    response = client.post(BREEDS_URL, data=breed_payload, format="json")

    assert response.status_code == HTTPStatus.CREATED, (
        "Проверьте, что при POST-запросе по адресу "
        f"{BREEDS_URL} создается новая порода собаки"
        f" и возвращается ответ со статусом {HTTPStatus.CREATED}."
    )

    assert Breed.objects.count() == 1, (
        "Проверьте, что при POST-запросе по адресу "
        f"{BREEDS_URL} создается новая порода собаки"
    )


@pytest.mark.django_db
@pytest.mark.parametrize(
    "invalid_data",
    [
        {"name": ""},
        {"size": ""},
        {"friendliness": 0},
        {"trainability": 0},
        {"shedding_amount": 0},
        {"exercise_needs": 0},
    ],
)
def test_create_breed_invalid_data(
    client: Client,
    invalid_data: dict[str, [str | int]],
) -> None:
    response = client.post(BREEDS_URL, data=invalid_data, format="json")
    assert response.status_code == HTTPStatus.BAD_REQUEST, (
        "Проверьте, что при POST-запросе по адресу "
        f"{BREEDS_URL} возвращается"
        f" ответ со статусом {HTTPStatus.BAD_REQUEST}."
    )
    assert not Breed.objects.count(), (
        "Проверьте, что при POST-запросе по адресу "
        f"{BREEDS_URL} не создается новая порода собаки"
    )


@pytest.mark.django_db
def test_delete_breed(client: Client, breed: Breed) -> None:
    response = client.delete(f"{BREEDS_URL}{breed.id}/")
    assert response.status_code == HTTPStatus.NO_CONTENT, (
        "Проверьте, что при DELETE-запросе по адресу "
        f"{BREEDS_URL}{breed.id} возвращается ответ со статусом "
        f"{HTTPStatus.NO_CONTENT}."
    )

    assert not Breed.objects.filter(id=breed.id).exists(), (
        "Проверьте, что при DELETE-запросе по адресу "
        f"{BREEDS_URL}{breed.id} удаляется порода собаки."
    )
