#!/usr/bin/python3
"""Unittest for BaseModel Class"""
import unittest
from datetime import datetime
import time
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """BaseModel Test Class"""
    def setUp(self):
        """Setup method"""
        self.b = BaseModel()

    def tearDown(self):
        """Teardown method"""
        del self.b

    def test_docstring(self):
        """Test docstring of the file"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_is_instance(self):
        """Test if object is instance of class"""
        self.assertIsInstance(self.b, BaseModel)
        self.assertIsInstance(self.b.created_at, datetime)
        self.assertIsInstance(self.b.updated_at, datetime)

    def test_id(self):
        """Test id"""
        self.assertTrue(hasattr(self.b, "id"))
        self.assertEqual(type(self.b.id), str)

    def test_save(self):
        """Test save method"""
        self.assertEqual(self.b.created_at, self.b.created_at)
        time.sleep(5)
        self.b.save()
        self.assertNotEqual(self.b.created_at, self.b.updated_at)

    def test_to_dict(self):
        """Test to_dict method"""
        self.assertEqual(self.b.to_dict()['__class__'], 'BaseModel')
