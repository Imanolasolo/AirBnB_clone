#!/usr/bin/python3
# File: amenity.py
# Authors: Imanol Asolo - Alex Arévalo
# email(s): <3848@holbertonschool.com>
#           <3915@holbertonschool.com>


"""This Module Defines the Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Inherits from BaseModel
    Represent an amenity.
    Attributes:
        name (str): The name of the amenity.
    """

    name = ""
