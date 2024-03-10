#!/usr/bin/python3
"""This file define the city class"""
from models.base_model import BaseModel


class City(BaseModel):
    """The class representing a city.

    Attributes:
        name (str): The city's name.
        state_id (str): The state's id.
    """

    name = ""
    state_id = ""
