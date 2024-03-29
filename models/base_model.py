#!/usr/bin/python3
"""Module for BaseModel class."""
import uuid
from datetime import datetime
import models


class BaseModel:
    """Defines the BaseModel class."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance."""
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        setattr(self, key, datetime.strptime(value, tform))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            now = datetime.now()
            self.created_at = now
            self.updated_at = now

    def __set_attributes(self, kwargs):
        """Set instance attributes from dictionary."""
        date_keys = ['created_at', 'updated_at']
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        for key, value in kwargs.items():
            if key in date_keys:
                value = datetime.strptime(value, tform)
            setattr(self, key, value)

    def __str__(self):
        """Update the updated_at attribute with current datetime."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)

    def save(self):
        """Update the updated_at attribute with current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary representation of BaseModel instance."""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
