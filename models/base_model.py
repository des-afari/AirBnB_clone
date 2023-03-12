#!/usr/bin/python3
"""Base Model Script"""
import uuid
from datetime import datetime


class BaseModel:
    """Base Model Class"""
    def __init__(self):
        """Gets called when you create an instance"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """String representation of a class"""
        return f"[{self.__class__.__name__}] ({self.id}) <{self.__dict__}>"

    def save(self):
        """Update updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all items of __dict__"""
        base_model_dict = self.__dict__.copy()

        base_model_dict['__class__'] = self.__class__.__name__
        base_model_dict['created_at'] = self.created_at.isoformat()
        base_model_dict['updated_at'] = self.updated_at.isoformat()

        return base_model_dict
