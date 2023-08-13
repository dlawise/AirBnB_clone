#!/usr/bin/python3

"""File defines the State Model
It inherits from the BaseModel
"""


from models.base_model import BaseModel


class State(BaseModel):
    """The State Model"""

    # Attributes
    name: str = ""
