from rental.transport.agricultural import Agricultural
from rental.transport.car import Car
from rental.transport.motorcycle import Motorcycle
from rental.transport.non_motor import Non_Motor


class VehicleFactory:
    def create_vehicle(self, vehicle_type, **kwargs):
        if vehicle_type == "car":
            return Car(**kwargs)
        elif vehicle_type == "motorcycle":
            return Motorcycle(**kwargs)
        elif vehicle_type == "agricultural":
            return Agricultural(**kwargs)
        elif vehicle_type == "non_motor":
            return Non_Motor(**kwargs)
        else:
            raise ValueError(f"Unknown vehicle type: {vehicle_type}")
