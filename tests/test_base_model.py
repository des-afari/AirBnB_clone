#!/usr/bin/python3
"""Tests for BaseModel"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import json


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def test_init(self):
        """Test case for __init__ method"""
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertTrue(hasattr(model, "id"))
        self.assertTrue(hasattr(model, "created_at"))
        self.assertTrue(hasattr(model, "updated_at"))
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_str(self):
        """Test case for __str__ method"""
        model = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(model.id, model.__dict__)
        self.assertEqual(str(model), expected_str)

    def test_save(self):
        """Test case for save method"""
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)

    def test_to_dict(self):
        """Test case for to_dict method"""
        model = BaseModel()
        dict_repr = model.to_dict()
        self.assertIsInstance(dict_repr, dict)
        self.assertEqual(dict_repr['__class__'], 'BaseModel')
        self.assertEqual(dict_repr['id'], model.id)
        self.assertEqual(dict_repr['created_at'], model.created_at.isoformat())
        self.assertEqual(dict_repr['updated_at'], model.updated_at.isoformat())

    def test_dict_to_instance_wrong_args(self):
        """Test case for creating instance from dictionary \
                with wrong arguments"""
        model = BaseModel()
        model_dict = model.to_dict()
        model_dict['id'] = 123
        with self.assertRaises(TypeError):
            new_model = BaseModel(**model_dict)
