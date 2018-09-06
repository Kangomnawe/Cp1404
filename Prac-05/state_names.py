"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
"""
STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
               "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
# print(STATE_NAMES)
state = input("Enter short state: ").upper()
while state != "":
    if state in STATE_NAMES:
        print(state, "is", STATE_NAMES[state])
    else:
        print("Invalid short state")
    state = input("Enter short state: ").upper()
"""

# dict = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
#         "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
#
# print(dict)
#
# print(dict['QLD'])
# print(dict['NSW'])
# print(dict['NT'])
# print(dict['WA'])
# print(dict['ACT'])
# print(dict['VIC'])
# print(dict['TAS'])

STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
               "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}

for index, state in enumerate(STATE_NAMES):
    print(index, state)

    # "{}.{:10}{:10}{:10}{:10}{:10}{:10}{:10}".format(index + 1, state[0], state[1], state[2], state[3], state[4],
    #                                                  state[5], state[6]))
