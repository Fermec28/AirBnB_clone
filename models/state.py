#!/usr/bin/python3
''' State Class'''
from .base_model import BaseModel


class State(BaseModel):
    '''
    Args:
    *args: Unused
    **kwargs: add the key-valua as attribute for the instance
    '''
    name = ""

    def __init__(self, *args, **kwargs):
        BaseModel.__init__(self, **kwargs)
