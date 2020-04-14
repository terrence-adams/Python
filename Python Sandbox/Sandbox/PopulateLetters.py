from Python.Classes.Letters import Letters
import string
import random

"""
This module is to demonstrate the import of a local module, a class created,
and to iterate through its properties and populate them.
By using the internal __dict__ of the class the attributes are assignable.
"""


def randomly_assign_letters():
    my_letters = Letters()
    i = 0
    for k, v in my_letters.__dict__.items():
        my_letters.__dict__[k] = random.choice(string.ascii_lowercase)
        i = i + 1
    print(my_letters.__dict__.items())  # print random dictionary of class instance


def alphabetical_order_letters():
    my_letters = Letters()
    i = 0
    for k, v in my_letters.__dict__.items():
        my_letters.__dict__[k] = string.ascii_lowercase[i]
        i = i + 1
    print(my_letters.__dict__.items())  # print ordered dictionary of class instance


if __name__ == '__main__':
    randomly_assign_letters()