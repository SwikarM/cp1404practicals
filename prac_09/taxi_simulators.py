# taxi_simulator.py
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]
    current_taxi = None
    total_bill = 0.0

    print("Let's drive!")

    while True:
        print(f"Bill to date: ${total_bill:.2f}")
        choice = input("q)uit, c)hoose taxi, d)rive\n>>> ").lower()

        if choice == 'q':
            break
        elif choice == 'c':
            display_taxis(taxis)
            try:
                taxi_choice = int(input("Choose taxi: "))
                if 0 <= taxi_choice < len(taxis):
                    current_taxi = taxis[taxi_choice]
                    print(f"You chose {current_taxi.name}")
                else:
                    print("Invalid taxi choice")
            except ValueError:
                print("Invalid input")
        elif choice == 'd':
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
                continue

            try:
                distance = float(input("Drive how far? "))
                current_taxi.start_fare()
                distance_driven = current_taxi.drive(distance)
                trip_cost = current_taxi.get_fare()
                total_bill += trip_cost
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
            except ValueError:
                print("Invalid distance")
        else:
            print("Invalid option")

    # Final output
    print(f"\nTotal trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Display available taxis with their details."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


if __name__ == '__main__':
    main()