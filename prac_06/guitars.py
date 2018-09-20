from prac_06.guitar_class import Guitar


def main():
    print("My Guitars!")
    guitars = []
    name = input("Name: ")

    while name != "":
        year = input("Year: ")
        cost = input("Cost: ")
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        name = input("Name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    # print(guitars)
    # add code to display a list of the guitars
    for guitar in guitars:
        print(guitar)


main()
