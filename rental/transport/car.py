from rental.transport.transport_base import Transport


class Car(Transport):
    def __init__(
        self, id, brand, model, year=None, color=None, engine_capacity=None, extra=None
    ):
        super().__init__(id, brand, model)
        self.year = year
        self.color = color
        self.engine_capacity = engine_capacity
        self.extra = extra

    def show_info(self):
        return (
            f"[CAR] {self.id}: {self.brand} {self.model} ({self.year}"
            f"{self.color}, {self.engine_capacity}L) - {self.extra}"
        )