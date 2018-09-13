"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

# from Prac-06

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("car1", 180)
    my_car.drive(30)
    print(my_car)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    # print(my_car)

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))

    limo = Car("limo", 100)
    print(limo)
    limo.add_fuel(20)
    print("fuel =", limo.fuel)

    limo = Car("limo 2", 120)
    print(limo)
    limo.drive(115)
    print("fuel =", limo.fuel)
    print("odo=", limo.odometer)

main()
