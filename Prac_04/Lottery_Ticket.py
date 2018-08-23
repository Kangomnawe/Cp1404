import random

NUMBER_EACH_LINE = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    number_quick_pick = int(input("How many numbers you picking?"))
    while number_quick_pick < 0:
        print("Not making any sense")
        number_quick_pick = int(input("How many numbers you picking"))
    for i in range(number_quick_pick):
        quick_pick = []
        for h in range(NUMBER_EACH_LINE):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in quick_pick:
                number = random.randint(MINIMUM, MAXIMUM)
            quick_pick.append(number)
        quick_pick.sort()
        print(quick_pick)


main()
