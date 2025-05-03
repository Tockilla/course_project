from rental.rental_records import RentalRecords
from datetime import datetime


def test_rental_record_creation():
    record = RentalRecords(vehicle_id="C001", customer_name="Jonas")
    assert record.vehicle_id == "C001"
    assert record.customer_name == "Jonas"
    assert isinstance(record.rent_time, datetime)


def test_rental_record_to_csv_row():
    record = RentalRecords(vehicle_id="C001", customer_name="Jonas", rent_time=datetime(2025, 4, 25, 15, 0))
    csv_row = record.to_csv_row()
    assert csv_row == "C001,Jonas,2025-04-25T15:00:00"
