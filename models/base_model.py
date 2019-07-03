#!/usr/bin/python3
''' BaseModel Class'''

import uuid
from datetime import datetime
import models


class BaseModel:
    '''
    Args:
    *args: Unused
    **kwargs: add the key-valua as attribute for the instance

    Attributes:
    id (str): This is the id of the instance,
    '''

    def __init__(self, *args, **kwargs):
        is_new = True
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        for key, value in kwargs.items():
            if key == "id":
                is_new = False
            if key != "__class__":
                if key == "created_at" or key == "updated_at":
                    setattr(self, key,
                            datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                else:
                    setattr(self, key, value)
                if hasattr(self.__class__, key):
                    aux = type(getattr(self.__class__, key))(value)
                    setattr(self, key, aux)
        if(is_new):
            models.storage.new(self)

    def __str__(self):
        '''
        Return string representation of the instance
        '''
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        '''
        Update update_at instance-s attribute
        '''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''
        Return:
        Dictionary representation of the instance to be deserializated
        '''
        dict_self = self.__dict__.copy()
        dict_self["__class__"] = self.__class__.__name__
        dict_self.update({'created_at': dict_self['created_at'].isoformat()})
        dict_self.update({'updated_at': dict_self['updated_at'].isoformat()})
        return dict_self

    def destroy(self):
        ''' call FileStorage to destroy the object'''
        models.storage.destroy(self)

    def update(self, att, val):
        ''' call FileStorage to destroy the object'''
        models.storage.update(self, att, val)