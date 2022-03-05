#!/usr/bin/python3
# File: review.py
# Authors: Imanol Asolo - Alex Arévalo
# email(s): <3848@holbertonschool.com>
#           <3915@holbertonschool.com>


"""This Module Defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Inherits from BaseModel.
    Represent a review.
    Attributes:
        place_id (str): The Place id.
        user_id (str): The User id.
        text (str): The text of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
