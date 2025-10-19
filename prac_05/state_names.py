"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania", "SA": "South Australia"}
print(STATE_NAMES)

state_code = input("Enter short state: ").upper()
if state_code in STATE_NAMES:
    print(f"{state_code} is {STATE_NAMES[state_code]}")
else:
    print("Invalid short state")

print("\nAll states:")
for code, name in STATE_NAMES.items():
    print(f"{code:3} is {name}")
