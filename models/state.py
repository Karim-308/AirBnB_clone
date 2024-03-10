from models.base_model import BaseModel

class State(BaseModel):
    """Defines the State class."""

    def __init__(self, *args, **kwargs):
        """Initialize State instance."""
        super().__init__(*args, **kwargs)
        self.name = ""
