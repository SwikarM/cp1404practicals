# unreliable_car.py
import random
from prac_09.car import Car


class UnreliableCar(Car):
    """A car that may or may not drive based on reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialize an UnreliableCar instance."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car only if it's reliable enough."""
        random_number = random.uniform(0, 100)
        if random_number < self.reliability:
            return super().drive(distance)
        else:
            return 0
