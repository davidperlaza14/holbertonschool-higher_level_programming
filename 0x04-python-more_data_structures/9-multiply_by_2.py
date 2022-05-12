#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = a_dictionary.copy()
    for c, b in new_dictionary.items():
        new_dictionary[c] = b * 2
    return(new_dictionary)
