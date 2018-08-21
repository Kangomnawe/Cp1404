def main():
    celsius = 10
    fahrenheit = 82

    print("Celcius and fahreheit")
    print(calculate_fahrenheit(celsius))
    print(calculate_celsius(fahrenheit))


def calculate_fahrenheit(celsius_):
    fahrenheit_input = (celsius_ * 1.8) + 32
    return fahrenheit_input


def calculate_celsius(fahrenheit_):
    celsius_input = (fahrenheit_ *1.8) + 32
    return celsius_input

main()
