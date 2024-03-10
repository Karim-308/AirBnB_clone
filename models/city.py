#!/usr/bin/python3



from models.base_model import BaseModel

class City(BaseModel):
    """Defines the City class."""
    
    state_id = ""  # Example attribute specific to City class
    name = ""      # Example attribute specific to City class

    def __init__(self, *args, **kwargs):
        """Initialize a new City instance."""
        super().__init__(*args, **kwargs)
        if kwargs:
            self.state_id = kwargs.get('state_id', "")
            self.name = kwargs.get('name', "")
