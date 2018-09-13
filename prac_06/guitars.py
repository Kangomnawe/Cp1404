from prac_06.guitar_class import Guitar


def main():
    print("My Guitars!")
    name = input("Name: ")
    guitars = []
    # for guitar in guitars:
    #     guitars.append(guitar)
    while name != "":
        guitars.append(input("Name:"))
        if guitars[-1] == "":
            guitars.pop()
            break

        # where we do the things we want to do in the loop

        # get year, cost
        # create guitar object
        # add guitar object to list of guitars
        # print message saying guitar has been added

        # name = input("Name: ")

    # print(guitars)
    # add code to display a list of the guitars
    for guitar in guitars:
        print(guitar)


main()
