"""
This script is a general overview of classes
"""

from dataclasses import dataclass


class BaseClass(object):  # Simple object class
    def __init__(self, *args, **kwargs):
        """
        :param args: define the arguments possible in detail here.
        :param kwargs: Accepts one, two, three, four and five as keyword arguments.
        """

        self.one = kwargs.get("one")
        self.two = kwargs.get("two")
        self.three = kwargs.get("three")
        self.four = kwargs.get("four")
        self.five = kwargs.get("five")

    def __repr__(self):
        return 'BaseClass({!r}, {!r}, {!r}, {!r}, {!r}'.format(
            self.one, self.two, self.three, self.four, self.five
        )

    def __str__(self):
        return f'One" {self.one}, Two" {self.two}, Three: {self.three}, Four: {self.four}, Five: {self.five}'


class ChildClass(BaseClass):  # Child class - inherits BaseClass
    def __init__(self, *args, **kwargs):
        """
        :param args: define the arguments possible in detail here.
        :param kwargs: Accepts six, seven, eight, nine, ten as keyword arguments.
        """
        super().__init__()  # Super is necessary to get the properties of the parent class

        self.six = kwargs.get("six")
        self.seven = kwargs.get("seven")
        self.eight = kwargs.get("eight")
        self.nine = kwargs.get("nine")
        self.ten = kwargs.get("ten")


class ChildOfChild(ChildClass):  # This class inherits the properties of ChildClass
    def __init__(self, *args, **kwargs):
        """
        :param args:
        :param kwargs:
        """
        super().__init__()

        self.eleven = kwargs.get("eleven")
        self.twelve = kwargs.get("twelve")
        self.thirteen = kwargs.get("thirteen")
        self.fourteen = kwargs.get("fourteen")
        self.fifteen = kwargs.get("fifteen")


"""
And so on, and so forth ...
"""


@dataclass  # The dataclass decorator (available in 3.7.2) automatically generates the __init__ and __repr__ methods.
class InventoryItem:
    """Class for keeping track of inventory items"""
    name: str
    price_per_unit: float
    inventory_quantity: int = 0


class CustomError(Exception):
    pass


def exception_test(x: int, y: int):
    try:
        if x + y <= 0:
            raise CustomError("The value is below 0")
        elif x + y == 0:
            raise CustomError("The value is 0")
        else:
            raise CustomError("The value is above 0")
    except CustomError:
        return

