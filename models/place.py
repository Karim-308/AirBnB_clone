#!/usr/bin/python3
"""this file is for Place class."""

from models.base_model import BaseModel

class Place(BaseModel):
    """Represent a place.

    Attributes:
        name (str): place name.
        description (str): place description.
        number_rooms (int): The number of rooms.
        city_id (str): City id.
        user_id (str): User id.
        price_by_night (int): price for nights.
        number_bathrooms (int): The number of bathrooms.
        max_guest (int): The maximum number of guests that can go in.
        longitude (float): The longitude of location.
        amenity_ids (list): A list of Amenity ids.
        latitude (float): The latitude.

    """

    def __init__(self, *args, **kwargs):
        """Initialize Place instance."""
        super().__init__(*args, **kwargs)
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []
