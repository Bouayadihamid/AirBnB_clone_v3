#!/usr/bin/python3
""" holds class User"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """Representation of a user """
    if models.storage_t == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user")
        reviews = relationship("Review", backref="user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
        if 'password' in kwargs:
            self.password = hashlib.md5(kwargs['password'].encode()).hexdigest()

    def set_password(self, password):
        """Hashes the password with MD5 and sets the user's password."""
        self.password = hashlib.md5(password.encode()).hexdigest()

    def to_dict(self, include_sensitive=False):
        """Convert user instance into dict format, possibly including password."""
        user_dict = super().to_dict(include_sensitive=include_sensitive)
        return user_dict
