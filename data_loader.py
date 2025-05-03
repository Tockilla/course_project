import csv
from rental.vehicle_factory import VehicleFactory

DEBUG = False


class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.factory = VehicleFactory()

    def load_vehicles(self):
        vehicles = []
        try:
            with open(self.file_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)

                for row in reader:
                    vehicle_type = row.get("type")

                    kwargs = {
                        "id": row.get("id"),
                        "brand": row.get("brand"),
                        "model": row.get("model"),
                        "year": row.get("year"),
                        "color": row.get("color"),
                        "engine_capacity": row.get("engine_capacity"),
                        "extra": row.get("extra")
                    }

                    try:
                        vehicle = self.factory.create_vehicle(vehicle_type, **kwargs)
                        vehicles.append(vehicle)
                    except ValueError as e:
                        if DEBUG:
                            print(f" Warning: {e} – skipping row: {row}")
        # debugas tam kad nelaudintu visos duomenu bazes man
                    except FileNotFoundError:
                           print(f" Error: File '{self.file_path}' not found.")
        except Exception as e:
            print(f" Unexpected error while loading vehicles: {e}")

        return vehicles
