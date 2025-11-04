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




main()