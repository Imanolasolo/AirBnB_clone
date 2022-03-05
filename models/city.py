#!/usr/bin/python3
# File: city.py
# Authors: Imanol Asolo - Alex Arévalo
# email(s): <3848@holbertonschool.com>
#           <3915@holbertonschool.com>


"""This Module Defines the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Inherits from BaseModel
    Represent a City.
    Attributes:
        state_id (str): The State id.
        name (str): The name of the city.
    """

    state_id = ""
    name = ""
