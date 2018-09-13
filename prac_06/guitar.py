from prac_06.guitar_class import Guitar


def main():
    test_guitar = Guitar("test guitar", 1978, 10000)
    print(test_guitar)
    print("{}".format(test_guitar))
    print(test_guitar.get_age())
    print(test_guitar.is_vintage())


main()
