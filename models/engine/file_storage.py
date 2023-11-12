#!usr/bin/python3

""" This is the File storage model handling storage and serialization """
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage():

    """
    This represents FileStorage class
    """

    __file_path = "file.json"
    __objects = {}
    __models = {
        'User': User,
        'BaseModel': BaseModel,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
    }

    def all(self):
        """
        This Returns all objects in BaseModel class representing format
        """
        return self.__objects

    def new(self, obj):
        """
        This is to Add obj to objects
        """
        self._objects[f"{obj.class.name_}.{obj.id}"] = obj

    def save(self):
        """"
        This Serializes objects in __objects to json objects and
        saves them in file.json file format
        """
        json_objs = {}
        for key, val in self.__objects.items():
            json_objs[key] = val.to_dict()
        with open(self.__file_path, "w", encoding='utf-8') as f:
            json.dump(json_objs, f, indent=4)

    def reload(self):
        """
        to Deserializes the JSON objects in file.json
        """
        try:
            with open(self.__file_path, "r", encoding='utf-8') as f:
                json_objs = json.load(f)

            for key, val in json_objs.items():
                constractor = val["_class_"]
                if val["_class"] in self._models.keys():
                    self._objects[key] = self.models[val["class_"]](
                        **val)
        except FileNotFoundError:
            pass
        except Exception as e:
            pass
