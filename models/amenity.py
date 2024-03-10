#!/usr/bin/python3
"""This file define an Amenity clas."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represent an amenity.

    Attributes:
        name (str): The amenity's name.
    """

    name = ""
