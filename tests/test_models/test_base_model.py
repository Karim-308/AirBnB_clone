# tests/test_models/test_base_model.py

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class."""

    def setUp(self):
        """Set up a BaseModel instance for testing."""
        self.base_model = BaseModel()

    def tearDown(self):
        """Clean up after each test."""
        del self.base_model

    def test_attributes_initialized(self):
        """Test if instance attributes are initialized properly."""
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertTrue(hasattr(self.base_model, 'updated_at'))

    def test_str_representation(self):
        """Test the __str__ method."""
        expected_str = "[BaseModel] ({}) {}".format(self.base_model.id, self.base_model.__dict__)
        self.assertEqual(str(self.base_model), expected_str)

    def test_save_method_updates_updated_at(self):
        """Test if the save method updates the updated_at attribute."""
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(old_updated_at, self.base_model.updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method."""
        model_dict = self.base_model.to_dict()
        self.assertTrue(isinstance(model_dict, dict))
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(type(model_dict['created_at']), str)
        self.assertEqual(type(model_dict['updated_at']), str)

    def test_constructor_with_kwargs(self):
        """Test if BaseModel can be created using **kwargs."""
        new_model = BaseModel(**self.base_model.to_dict())
        self.assertEqual(self.base_model.id, new_model.id)
        self.assertEqual(self.base_model.created_at, new_model.created_at)
        self.assertEqual(self.base_model.updated_at, new_model.updated_at)


if __name__ == '__main__':
    unittest.main()
