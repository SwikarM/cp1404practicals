"""
Hex Colours Lookup
Estimate: 15 minutes
Actual:   (record your actual time here)
"""


HEX_COLOURS = {   "ALICEBLUE": "#f0f8ff",
    "ANTIQUEWHITE": "#faebd7",
    "AQUA": "#00ffff",
    "AZURE": "#f0ffff",
    "BEIGE": "#f5f5dc",
    "BLACK": "#000000",
    "BLUE": "#0000ff",
    "BROWN": "#a52a2a",
    "CHOCOLATE": "#d2691e",
    "CORAL": "#ff7f50" }

def main():
    """Look up hexadecimal colour codes by name."""
    while True:
        colour_name = input("Enter a colour name: ").strip()
        if colour_name == "":
            break
        colour_code = HEX_COLOURS.get(colour_name.upper())
        if colour_code:
            print(f"{colour_name.title()} is {colour_code}")
        else:
            print("Invalid colour name")

main()