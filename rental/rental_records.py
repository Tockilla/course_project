from datetime import datetime


class RentalRecords:
    def __init__(self, vehicle_id, customer_name, rent_time=None):
        self.vehicle_id = vehicle_id
        self.customer_name = customer_name
        self.rent_time = rent_time if rent_time else datetime.now()

    def to_csv_row(self):
   
        return f"{self.vehicle_id},{self.customer_name},{self.rent_time.isoformat()}"
