#!usr/bin/python3

""" This is a File storage model """
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.review import Review
from models.city import City
from models.amenity import Amenity



class FileStorage():

    """
    This is a FileStorage class
    """

    __file_path = "file.json"
    __objects = {}
    __models = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'Place': Place,
        'Review': Review
        'City': City,
        'Amenity': Amenity,
        
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
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """"
        To Serialize objects in __objects to json objects and
        to save them in file.json file format
        """
        json_objs = {}
        for key, val in self.__objects.items():
            json_objs[key] = val.to_dict()
        with open(self.__file_path, "w", encoding='utf-8') as f:
            json.dump(json_objs, f, indent=4)

    def reload(self):
        """
        To Deserializes the JSON objects in file.json
        """
        try:
            with open(self.__file_path, "r", encoding='utf-8') as f:
                json_objs = json.load(f)

            for key, val in json_objs.items():
                constractor = val["__class__"]
                if val["__class__"] in self.__models.keys():
                    self.__objects[key] = self.__models[val["__class__"]](
                        **val)
        except FileNotFoundError:
            pass
        except Exception as e:
            pass
