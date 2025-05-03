from rental.rental_manager import RentalManager
from rental.data_loader import DataLoader


def main():
    loader = DataLoader("data/vehicles.csv")
    vehicles = loader.load_vehicles()
    manager = RentalManager(vehicles)

    while True:
        print("\n=== Transport Rental System ===")
        print("1. Show all vehicles")
        print("2. Search vehicle by ID")
        print("3. Rent a vehicle")
        print("4. Cancel rental: ")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            manager.display_vehicles()
        elif choice == "2":
            vehicle_id = input("Enter vehicle ID: ")
            manager.show_vehicle(vehicle_id)
        elif choice == "3":
            vehicle_id = input("Enter vehicle ID to rent: ")
            customer_name = input("Enter customer name: ")
            manager.rent_vehicle(vehicle_id, customer_name)
        elif choice == "4":
            vehicle_id = input("Enter vehicle ID to cancel rental: ")
            manager.cancel_rental(vehicle_id)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
