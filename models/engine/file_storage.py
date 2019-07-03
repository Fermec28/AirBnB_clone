#!/usr/bin/python3
''' File storage Class'''

import json
from ..user import User
from ..base_model import BaseModel
from ..state import State
from ..city import City
from ..amenity import Amenity
from ..place import Place
from ..review import Review


class FileStorage():
    '''
    Class to save the data in .json file
    '''

    __file_path = 'file.json'
    __objects = {}
    validClasses = {
        "BaseModel": BaseModel,
        "User": User
    }

    def all(self):
        '''Return all the objects created '''
        return self.__objects

    def new(self, obj):
        '''sets in __objects the obj with key <obj class name>.id'''
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        '''serializes __objects to the JSON file (path: __file_path)'''
        copy_db = {}
        for k, v in self.__objects.items():
            copy_db[k] = self.__objects[k].to_dict()
        with open(self.__file_path, 'w') as outfile:
            json.dump(copy_db, outfile)

    def reload(self):
        '''deserializes the JSON file to __objects'''
        try:
            with open(self.__file_path) as json_file:
                data = json.load(json_file)
                for k, v in data.items():
                    key = "{}.{}".format(v["__class__"], v["id"])
                    value = self.validClasses[v["__class__"]](**v)
                    self.__objects[key] = value
        except IOError:
            pass

    def destroy(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        del(self.__objects[key])
        self.save()
