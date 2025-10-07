"""
CP1404/CP5632 - Practical
Menus
"""

def main():
    name = input("Enter name: ")

    # Display menu and get initial choice
    choice = input_menu()

    while choice != "Q":
        if choice == "H":
            print(f"Hello {name}")
        elif choice == "G":
            print(f"Goodbye {name}")
        else:
            print("Invalid choice")

        choice = input_menu()
    print("Finished.")


def input_menu():
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")
    return input(">>> ").upper()



main()