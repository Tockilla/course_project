from abc import ABC, abstractmethod


class Transport(ABC):
    def __init__(self, id, brand, model):
        self.id = id
        self.brand = brand
        self.model = model
        self._rental_status = "available"

    @abstractmethod
    def show_info(self):
        pass

    @property
    def rental_status(self):
        return self._rental_status

    def rent(self):
        if self._rental_status == "rented":
            raise Exception(f"Vehicle {self.id} is already rented.")
        self._rental_status = "rented"

    def return_vehicle(self):
        if self._rental_status == "available":
            raise Exception(f"Vehicle {self.id} is already available.")
        self._rental_status = "available"
