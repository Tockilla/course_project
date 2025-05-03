import pytest
from rental.transport.car import Car


def test_car_initialization():
    car = Car(
        id="C001",
        brand="Toyota",
        model="Corolla",
        year=2020,
        color="Red",
        engine_capacity=1.8,
        extra="GPS",
    )

    assert car.id == "C001"
    assert car.brand == "Toyota"
    assert car.model == "Corolla"
    assert car.year == 2020
    assert car.color == "Red"
    assert car.engine_capacity == 1.8
    assert car.extra == "GPS"


def test_car_show_info():
    car = Car(
        id="C001",
        brand="Toyota",
        model="Corolla",
        year=2020,
        color="Red",
        engine_capacity=1.8,
        extra="GPS",
    )

    info = car.show_info()
    assert "[CAR] C001" in info
    assert "Toyota" in info

    assert "Red" in info
