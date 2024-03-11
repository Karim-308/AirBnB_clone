# models/engine/file_storage.py
"""This file defines the file storage"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Save the objects to the JSON file. , TOBE checked again"""
        with open(self.__file_path, "w") as file:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, file)

 
    def reload(self):
        """Reload the objects from the JSON file. TOBE checked again """
        try:
            with open(self.__file_path, "r") as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    cls = eval(class_name)
                    self.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass
