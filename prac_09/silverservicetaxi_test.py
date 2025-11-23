# silver_service_taxi_test.py
from silver_service_taxi import SilverServiceTaxi


def test_silver_service_taxi():
    # Test with fanciness of 2
    fancy_taxi = SilverServiceTaxi("Hummer", 200, 2)

    # Test initial state
    print("Initial state:")
    print(fancy_taxi)
    print(f"Initial fare: ${fancy_taxi.get_fare():.2f}")
    print()

    # Test fare calculation
    fancy_taxi.drive(18)
    fare = fancy_taxi.get_fare()
    print(f"After 18km trip:")
    print(fancy_taxi)
    print(f"Fare: ${fare:.2f}")

    # Test expected fare
    expected_fare = (18 * (1.23 * 2)) + 4.50
    expected_fare = round(expected_fare, 1)  # Rounded to nearest 10c
    print(f"Expected fare: ${expected_fare:.2f}")
    print(f"Fare matches expected: {abs(fare - expected_fare) < 0.01}")


if __name__ == '__main__':
    test_silver_service_taxi()