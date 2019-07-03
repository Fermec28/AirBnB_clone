#!/usr/bin/python3
''' Place Class'''
from .base_model import BaseModel


class Place(BaseModel):
    '''
    Args:
    *args: Unused
    **kwargs: add the key-valua as attribute for the instance
    '''
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = [""]

    def __init__(self, *args, **kwargs):
        BaseModel.__init__(self, **kwargs)
