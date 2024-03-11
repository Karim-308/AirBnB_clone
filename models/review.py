#!/usr/bin/python3
"""Defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """This is a review class definition.

    Attributes:
        user_id (str): The User id.
        text (str): The text of the review.
        place_id (str): The Place id.

    """

    user_id = ""
    place_id = ""
    text = ""
