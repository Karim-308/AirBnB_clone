#!/usr/bin/python3
"""this file define the State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """Represent a state class definition.

    Attributes:
        name (str): The state name.
    """

    name = ""
