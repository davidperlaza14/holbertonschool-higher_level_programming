#!/usr/bin/python3
"""base
"""


import json
from re import S


class Base:
    """Base of the other shapes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string representation
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes to file with JSON string
        """

        with open(cls.__name__ + ".json", mode="w") as write_file:
            if list_objs is None:
                write_file.write("[]")
            else:
                # Using to_json_string(), and to_dictionary() to format
                write_file.write(cls.to_json_string(
                                 [item.to_dictionary() for item in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        '''
        Returns list of
        dictionaries from JSON
        '''
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''
        Returns instance with
        all attributes set
        '''
        if cls.__name__ == 'Rectangle':
            newInstance = cls(1, 1)
            newInstance.update(**dictionary)
            return newInstance
        if cls.__name__ == 'Square':
            newInstance = cls(1)
            newInstance.update(**dictionary)
            return newInstance
        else:
            return None

    @classmethod
    def load_from_file(cls):
        '''
        Returns a list
        of instances
        '''
        instanceList = []
        try:
            with open('{}.json'.format(cls.__name__), 'r',
                      encoding='utf-8') as f:
                objectList = cls.from_json_string(f.read())
        except IOError:
            return []
        for dictionary in objectList:
            instanceList.append(cls.create(**dictionary))
        return instanceList