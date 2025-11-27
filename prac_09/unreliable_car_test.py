# unreliable_car_test.py
from unreliable_car import UnreliableCar


def main():
    # Create an unreliable car with 50% reliability
    unreliable_car = UnreliableCar("Old Clunker", 100, 50.0)

    # Test driving multiple times
    successful_drives = 0
    total_attempts = 100

    for i in range(total_attempts):
        unreliable_car.start_fare() if hasattr(unreliable_car, 'start_fare') else None
        distance_driven = unreliable_car.drive(10)
        if distance_driven > 0:
            successful_drives += 1

    success_rate = (successful_drives / total_attempts) * 100
    print(f"Car drove successfully {successful_drives} out of {total_attempts} times")
    print(f"Success rate: {success_rate:.1f}% (expected around 50%)")

    # Test with high reliability car
    reliable_car = UnreliableCar("New Car", 100, 90.0)
    reliable_car.drive(10)
    print(f"\nReliable car drove: {reliable_car.fuel} fuel remaining")

main()