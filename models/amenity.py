#!/usr/bin/python3
''' Amenity Class'''
from .base_model import BaseModel


class Amenity(BaseModel):
    '''
    Args:
    *args: Unused
    **kwargs: add the key-valua as attribute for the instance
    '''
    name = ""

    def __init__(self, *args, **kwargs):
        BaseModel.__init__(self, **kwargs)
