#!/usr/bin/python3
"""inherits_from funtion
"""

def inherits_from(obj, a_class):
    """
    Write a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.
    """

    if type(obj) is a_class or not isinstance(obj, a_class):
        return False
    else:
        return True
