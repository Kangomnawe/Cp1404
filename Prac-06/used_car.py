"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

# from Prac-06
from Prac-06.car import car


def main():
    """Demo test code to show how to use car class."""
    my_car = car(180)
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))


main()