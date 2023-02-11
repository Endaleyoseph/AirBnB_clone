#!/usr/bin/python3

"""module named user
"""

from models.base_model import BaseModel


class User(BaseModel):

    """class User inherited from base model named BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
