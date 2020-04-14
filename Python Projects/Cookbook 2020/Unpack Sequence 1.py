# sample grade example
import statistics  # required for built in math functions

"""
This method unpacks the iterable, and returns an average of the collection, by ignoring the first and last
It makes use of the * variable assignment

"""


def drop_first_last(grades):
    first, *middle, last = grades
    print(type(middle))  # This is expected to be a list
    return statistics.mean(middle)

values = [76,89,99,100,58,69,85,81,91,92]
print("The grade average is", drop_first_last(values))