from prac_06.guitar_class import Guitar


def main():
    print("My Guitars!")
    guitars = []
    guitar_model =input("namer:")
    while guitar_model != "":
        name = input("Name:")
        year = input("Year:")
        cost = input("Cost")
        if name == "":
            break
        # else:
        #     guitars.append(name)
        #     guitars = sorted(guitars)
        #     # print(guitars)

    # where we do the things we want to do in the loop

        # get year, cost
        # create guitar object
        # add guitar object to list of guitars
        # print message saying guitar has been added

        # name = input("Name: ")

    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    # print(guitars)
    # add code to display a list of the guitars
    for guitar in guitars:
        print(guitar)


main()
