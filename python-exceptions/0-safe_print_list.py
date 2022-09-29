#!/usr/bin/python3
from ast import Try


def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        while count < x:
            print("{}".format(my_list[count]), end='')
            count += 1
        print()
        return count

    except IndexError:
        print()
        return count
        pass
