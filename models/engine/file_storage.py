#!/usr/bin/python3
"""Creating a class for storing all the created objects of a class"""


import json
from models.base_model import BaseModel


class FileStorage:
    """class for serializing and deserializing data of instances"""
    """stores objects by <class name>.id"""
    __objects = {}
    """path to JSON file"""
    __file_path = "file.json"

    def all(self):
        """returns the dictionary of objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects with key<obj class name.id>"""
        if obj is not None:
            key = obj.__class__.__name__+"."+obj.id
            self.__objects[key] = obj

    def save(self):
        """method for serializing __objects to a JSON file"""
        data_dict = {}
        for key in self.__objects:
            data_dict[key] = self.__objects[key].to_dict()
            """serializing the data"""
            with open(self.__file_path, 'w') as f:
                json.dump(data_dict, f)

    def reload(self):
        """method for deserializing a json file if file exists"""
        try:
            with open(self.__file_path, 'r') as f:
                data_dict = json.load(f)
            for data in data_dict.values():
                class_name = data["__class__"]

            del data[__class__]
            self.new(eval(class_name)(**data))

        except FileNotFoundError:
            pass
