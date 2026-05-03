from academy.practice.vehicle import Vehicle


class Car(Vehicle):
    value = 50000

    def __init__(self, wheels, speed, doors):
        super().__init__(wheels, speed)
        self.doors = doors

    def race(self):
        print(f"car is racing at {self.speed} miles/hr")

    @staticmethod
    def test():
        return f"this is static"

    @classmethod
    def test_class_method(cls):
        return f"Cost: {cls.value}"

    def __repr__(self):
        return f"Car has {self.wheels} wheels, {self.doors} doors and drives at {self.speed} miles/hr"