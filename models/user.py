#!/usr/bin/python3
''' User Class'''
from .base_model import BaseModel


class User(BaseModel):
    '''
    Args:
    *args: Unused
    **kwargs: add the key-valua as attribute for the instance

    Attributes:
    id (str): This is the id of the instance,
    '''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    def __init__(self, *args, **kwargs):
        BaseModel.__init__(self,**kwargs)
