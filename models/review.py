#!/usr/bin/python3

"""module named review
"""

from models.base_model import BaseModel


class Review(BaseModel):

    """class Review inherited from base model named BaseModel"""

    place_id = ""
    user_id = ""
    text = ""
