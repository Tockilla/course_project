import pytest
from rental.transport.car import Car  # arba Motorcycle, Agricultural...


def test_rent_available_vehicle():
    car = Car(id="C001", brand="Toyota", model="Corolla", year=2020, color="Blue", engine_capacity=1.8)
    assert car.rental_status == "available"
    car.rent()
    assert car.rental_status == "rented"


def test_rent_already_rented_vehicle():
    car = Car(id="C001", brand="Toyota", model="Corolla", year=2020, color="Blue", engine_capacity=1.8)
    car.rent()
    with pytest.raises(Exception, match="already rented"):
        car.rent()


def test_return_rented_vehicle():
    car = Car(id="C001", brand="Toyota", model="Corolla", year=2020, color="Blue", engine_capacity=1.8)
    car.rent()
    car.return_vehicle()
    assert car.rental_status == "available"


def test_return_available_vehicle_raises_error():
    car = Car(id="C001", brand="Toyota", model="Corolla", year=2020, color="Blue", engine_capacity=1.8)
    with pytest.raises(Exception, match="already available"):
        car.return_vehicle()
