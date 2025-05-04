import pytest
from rental.transport.car import Car
from rental.rental_manager import RentalManager
import os


def test_cancel_rental(tmp_path):

    car = Car(
        id="C001",
        brand="Toyota",
        model="Corolla",
        year=2020,
        color="Blue",
        engine_capacity=1.8,
    )
    car.rent()  


    rental_file = tmp_path / "data" / "rental.csv"
    os.makedirs(rental_file.parent, exist_ok=True)
    rental_file.write_text("C001,Jonas,2025-04-25T15:00:00\n")


    manager = RentalManager([car], rental_file_path=rental_file)

    manager.cancel_rental(vehicle_id="C001")


    assert car.rental_status == "available"


    with open(rental_file, "r") as file:
        contents = file.read()
        assert contents.strip() == ""
