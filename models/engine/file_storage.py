#!/usr/bin/python3
"""This file defines the file storage"""
import json
import sys
import errno
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """This represents an abstraction for storage engine

    Attributes:
        __file_path (str): which file to save to.
        __objects (dict): represents the dictionary of created objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return dictionary  for all __objects."""
        return self.__objects

    def new(self, obj):
        """Set in <obj_class_name>.id"""        
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Save the objects to the JSON file. , TOBE checked again"""
        with open(self.__file_path, "w") as file:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, file)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            if os.path.exists(self.__file_path):
                with open(self.__file_path, "r") as f:
                    objdict = json.load(f)
                    for o in objdict.values():
                        cls_name = o.get("__class__")
                        if cls_name:
                            del o["__class__"]
                            self.new(eval(cls_name)(**o))
        except Exception as e:
		print("Error loading JSON file: {}".format(e))
