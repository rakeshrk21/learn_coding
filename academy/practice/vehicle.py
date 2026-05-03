from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, wheels, speed):
        self.wheels = wheels
        self.speed = speed

    def __repr__(self):
        return f"Vehicle with {self.wheels} wheels and can ride with speed {self.speed} miles/hr"

    @abstractmethod
    def race(self):
        pass