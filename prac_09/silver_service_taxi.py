# silver_service_taxi.py
from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """A fancy taxi with additional flagfall charge."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialize a SilverServiceTaxi instance."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        """Return the price for the taxi trip including flagfall."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return a string representation including flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"