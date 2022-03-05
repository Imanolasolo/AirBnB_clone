#!/usr/bin/python3
# File: state.py
# Authors: Imanol Asolo - Alex Arévalo
# email(s): <3848@holbertonschool.com>
#           <3915@holbertonschool.com>


"""This Module Defines the State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Inherits from BaseModel
    Represent a State.
    Attributes:
        name (str): The name of the State.
    """

    name = ""
