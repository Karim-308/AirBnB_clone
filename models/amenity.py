#!/usr/bin/python3
from models.base_model import BaseModel

class Amenity(BaseModel):
    """Defines the Amenity class."""

    def __init__(self, *args, **kwargs):
        """Initialize Amenity instance."""
        super().__init__(*args, **kwargs)
        self.name = ""
