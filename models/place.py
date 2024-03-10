#!/usr/bin/python3
"""This file defines the code for the place code."""
from models.base_model import BaseModel


class Place(BaseModel):
    """This class represents the place.

    Attributes:
        user_id (str): User's id.
        city_id (str): City's id.
        name (str): place's name.
        latitude (float): The latitude of the place's latitude.
        longitude (float): The longitude of the place's longitude.
        description (str): the place's description.
        number_rooms (int): the place's number of rooms.
        price_by_night (int): night's price.
        number_bathrooms (int): the place's number of bathrooms.
        max_guest (int): the place's maximum number of guests.
        amenity_ids (list): Amenity ids list.
    """


    user_id = ""
    city_id = ""
    name = ""
    latitude = 0.0
    longitude = 0.0
    description = ""
    number_rooms = 0
    price_by_night = 0
    number_bathrooms = 0
    max_guest = 0
    amenity_ids = []
