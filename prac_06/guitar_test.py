from prac_06.guitar_class import Guitar


def main():
    guitar_1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar_2 = Guitar("Another Guitar", 2012, 23100.23)

    print("{} get_age() - Expected 96 . got  {}".format(guitar_1.name, guitar_1.get_age()))
    print("{} get_age() - Expected 6. got {}".format(guitar_2.name, guitar_2.get_age()))
    # print(guitar_1.is_vintage())
    print("Gibson L-5 CES is_vintage()- Expected True. got {}".format(guitar_1.is_vintage()))
    print("Another Guitar is_vintage() - Expected False. got {}".format(guitar_2.is_vintage()))


main()
