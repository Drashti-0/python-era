class vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


class car(vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats
        print(self.seats)


class bike(vehicle):
    def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model)
        self.engine_cc = engine_cc
        print(self.engine_cc)


v1 = car("Toyota", "Fortuner", 7)
v2 = bike("Honda", "Shine", 125)