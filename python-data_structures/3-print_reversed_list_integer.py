#!/usr/bin/python3
from symbol import return_stmt


def print_reversed_list_integer(my_list=[]):
    for index in my_list[::-1]:
        print("{:d}".format(index))
    