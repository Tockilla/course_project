from rental.transport.transport_base import Transport

class Agricultural(Transport):
    def __init__(self, id, brand, model, year=None, color=None, engine_capacity=None, extra=None):
        super().__init__(id, brand, model)
        self.year = year
        self.color = color
        self.engine_capacity = engine_capacity  # gali būti None
        self.extra = extra

    def show_info(self):
        return (f"[AGRICULTURAL] {self.id}: {self.brand} {self.model} "
                f"({self.year}, {self.color}, {self.engine_capacity or 'N/A'}L, {self.extra})")
