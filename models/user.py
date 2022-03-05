#!/usr/bin/python3
# File: user.py
# Authors: Imanol Asolo - Alex Arévalo
# email(s): <3848@holbertonschool.com>
#           <3915@holbertonschool.com>


"""This Module Defines the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Inherits from BaseModel.
    Represent a User.
    Attributes:
        email (str): The email of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
