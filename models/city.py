#!/usr/bin/python3
''' City Class'''
from .base_model import BaseModel


class City(BaseModel):
    '''
    Args:
    *args: Unused
    **kwargs: add the key-valua as attribute for the instance

    '''
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        BaseModel.__init__(self, **kwargs)
