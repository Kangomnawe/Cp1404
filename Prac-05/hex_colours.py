"""
Exa_colours

"""

COLOUR_CODES = {"WHITE": "#FFFFFF", "BLACK": "#000000", "RED": "#FF0000", "MAROON": "#800000",
                "YELLOW": "#FFFF00", "OLIVE": "#808000", "LIME": "#00FF00", "GREEN": "#008000", "BLUE": "#0000FF",
                "NAVY": "#000080", "FUCHSIA": "##FF00FF", "PURPLE": "#800080"}
# print(STATE_NAMES)

colour = input("Enter short colour: ").upper()
while colour != "":
    if colour in COLOUR_CODES:
        print(colour, "is", COLOUR_CODES[colour])
    else:
        print("Invalid short colour")
    colour = input("This colour, we don't have in the list: ").upper()

