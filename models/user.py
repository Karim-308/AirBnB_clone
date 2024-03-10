#!/usr/bin/python3
"""The file defines the user class."""
from models.base_model import BaseModel


class User(BaseModel):
    """This class represents a user.

    Attributes:
        first_name (str): the user's first name.
        last_name (str): the user's last name.
        email (str): the user's email.
        password (str): the user's password.
    """

    first_name = ""
    last_name = ""
    email = ""
    password = ""
