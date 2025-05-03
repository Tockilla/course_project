from rental.rental_records import RentalRecords


class RentalManager:
    def __init__(self, vehicles=None, rental_file_path="data/rental.csv"):
        self.vehicles = vehicles if vehicles else []
        self.rental_file_path = rental_file_path

    def display_vehicles(self):
        print("\n--- Available Vehicles ---")
        for vehicle in self.vehicles:
            print(vehicle.show_info())

    def show_vehicle(self, vehicle_id):
        for vehicle in self.vehicles:
            if vehicle.id == vehicle_id:
                print(vehicle.show_info())
                return
        print("Vehicle not found.")

    def rent_vehicle(self, vehicle_id, customer_name):
        for vehicle in self.vehicles:
            if vehicle.id == vehicle_id:
                if self._is_vehicle_rented(vehicle_id):
                    print("Vehicle is already rented (based on records).")
                    return
                vehicle.rent()
                record = RentalRecords(vehicle_id, customer_name)
                self._save_rental_record(record)
                print(f"Vehicle {vehicle_id} rented successfully to {customer_name}.")
                return
        print("Vehicle not found.")

    def _save_rental_record(self, record):
        with open(self.rental_file_path, "a") as file:
            file.write(record.to_csv_row() + "\n")

    def _is_vehicle_rented(self, vehicle_id):
        try:
            with open(self.rental_file_path, "r") as file:
                for line in file:
                    rented_id = line.strip().split(",")[0]
                    if rented_id == vehicle_id:
                        return True
            return False
        except FileNotFoundError:
            return False

    def cancel_rental(self, vehicle_id):
        found = False

        try:
            with open(self.rental_file_path, "r") as file:
                lines = file.readlines()
        except FileNotFoundError:
            print("No rentals found.")
            return

        with open(self.rental_file_path, "w") as file:
            for line in lines:
                if not line.startswith(vehicle_id + ","):
                    file.write(line)
                else:
                    found = True

        if found:
            for vehicle in self.vehicles:
                if vehicle.id == vehicle_id:
                    if vehicle.rental_status == "rented":
                        vehicle.return_vehicle()
                        print(
                            f"Rental for vehicle {vehicle_id} cancelled successfully."
                        )
                    else:
                        print(
                            f"Rental for vehicle {vehicle_id} cancelled successfully."
                        )
                    return
            print("Vehicle ID found in rental file but not in current system.")
        else:
            print(f"No active rental found for vehicle {vehicle_id}.")
