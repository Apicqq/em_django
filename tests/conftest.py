from mixer.backend.django import mixer
import pytest

from dogs.models import Breed, Dog


@pytest.fixture
def breed_list() -> list[Breed]:
    return mixer.cycle(10).blend("dogs.Breed")


@pytest.fixture
def breed() -> Breed:
    return mixer.blend("dogs.Breed")


@pytest.fixture
def breed_payload() -> dict[str, [str | int]]:
    return dict(
        name="Такса",
        size="Large",
        friendliness=5,
        trainability=3,
        shedding_amount=2,
        exercise_needs=4,
    )


@pytest.fixture
def dog(breed: Breed) -> Dog:
    return mixer.blend("dogs.Dog", breed=breed)


@pytest.fixture
def dogs_list(breed: Breed) -> list[Dog]:
    return mixer.cycle(10).blend("dogs.Dog", breed=breed)


@pytest.fixture
def dog_payload(breed: Breed) -> dict[str, [str | int]]:
    return dict(
        name="Sobaka",
        age=5,
        breed=breed.id,
        gender="Male",
        color="Black",
        favorite_food="Meat",
        favorite_toy="Ball",
    )
