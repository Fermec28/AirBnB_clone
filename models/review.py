#!/usr/bin/python3
''' Review Class'''
from .base_model import BaseModel


class Review(BaseModel):
    '''
    Args:
    *args: Unused
    **kwargs: add the key-valua as attribute for the instance
    '''
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        BaseModel.__init__(self, **kwargs)
