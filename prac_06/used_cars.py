"""
CP1404/CP5632 Practical - Client code to use the Car class.

"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180)
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)

    # Create a new Car object called "limo" that is initialised with 100 units of fuel
    limo = Car("Limo", 100)

    # Add 20 more units of fuel to this new car object using the add method
    limo.add_fuel(20)

    # Print the amount of fuel in the car
    print(f"Limo has fuel: {limo.fuel}")

    # Attempt to drive the car 115 km using the drive method
    distance_driven = limo.drive(115)
    print(f"Limo drove {distance_driven}km")

    print(my_car)
    print(limo)


main()