#!/usr/bin/python3
"""Class User that inherits from class BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """Inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
