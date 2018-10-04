"""
CP1404/CP5632 Practical - Suggested Solution
SilverServiceTaxi class, derived from Taxi
"""

from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Represent a SilverServiceTaxi."""
    flagfall = 4.5

    # noinspection PyArgumentList
    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi.
        :rtype: flagfall
        """
        super().__init__(name, fuel)
        self.price_per_km = fanciness * Taxi.price_per_km

    def __str__(self):
        """Return a string representation of a SilverServiceTaxi."""
        return "{} plus flagfall of ${:.2f}".format(super().__str__(),
                                                    self.flagfall)

    def get_fare(self):
        """Get the current fare."""
        return self.flagfall + super().get_fare()
