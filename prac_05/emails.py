"""
Emails
Estimate: 20 minutes
Actual:   (record your actual time here)
"""
def main():
    """Store emails and names in a dictionary."""
    email_to_name = {}

    email = input("Email: ").strip()
    while email != "":
        name = extract_name(email)
        confirm = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if confirm not in ("", "y"):
            name = input("Name: ").title()

        email_to_name[email] = name
        email = input("Email: ").strip()

    print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name(email):
    """Extract a name from an email address."""
    prefix = email.split("@")[0]
    parts = prefix.split(".")
    name = " ".join(parts).title()
    return name


main()