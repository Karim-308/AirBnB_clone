#!/usr/bin/python3
"""Module to test the console."""

import unittest
import sys
import os
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from unittest.mock import patch


class TestConsole(unittest.TestCase):
    """Test cases for the console."""

    def setUp(self):
        """Set up the test environment."""
        self.console = HBNBCommand()

    def tearDown(self):
        """Tear down the test environment."""
        del self.console

    @patch('sys.stdout', new_callable=StringIO)
    def test_create(self, mock_stdout):
        """Test the create command."""
        self.console.onecmd("create User")
        output = mock_stdout.getvalue().strip()
        self.assertIn("User.", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_show(self, mock_stdout):
        """Test the show command."""
        self.console.onecmd("create User")
        obj_id = mock_stdout.getvalue().strip().split()[0]
        self.console.onecmd("show User {}".format(obj_id))
        output = mock_stdout.getvalue().strip()
        self.assertIn(obj_id, output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy(self, mock_stdout):
        """Test the destroy command."""
        self.console.onecmd("create User")
        obj_id = mock_stdout.getvalue().strip().split()[0]
        self.console.onecmd("destroy User {}".format(obj_id))
        with patch('sys.stdout', new=StringIO()) as mock_out:
            self.console.onecmd("show User {}".format(obj_id))
            output = mock_out.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_update(self, mock_stdout):
        """Test the update command."""
        self.console.onecmd("create User")
        obj_id = mock_stdout.getvalue().strip().split()[0]
        self.console.onecmd("update User {} first_name 'John'".format(obj_id))
        with patch('sys.stdout', new=StringIO()) as mock_out:
            self.console.onecmd("show User {}".format(obj_id))
            output = mock_out.getvalue().strip()
            self.assertIn("John", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_count(self, mock_stdout):
        """Test the count command."""
        self.console.onecmd("create User")
        self.console.onecmd("create User")
        self.console.onecmd("count User")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "2")

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_with_count(self, mock_stdout):
        """Test the destroy command with count."""
        self.console.onecmd("create User")
        obj_id = mock_stdout.getvalue().strip().split()[0]
        self.console.onecmd("destroy User {}".format(obj_id))
        self.console.onecmd("count User")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "0")

    @patch('sys.stdout', new_callable=StringIO)
    def test_all_base_model(self, mock_stdout):
        """Test the all command for BaseModel."""
        self.console.onecmd("create BaseModel")
        self.console.onecmd("create BaseModel")
        self.console.onecmd("BaseModel.all()")
        output = mock_stdout.getvalue().strip()
        self.assertIn("BaseModel", output)
        self.assertIn("2", output)
    @patch('sys.stdout', new_callable=StringIO)
    def test_all_review(self, mock_stdout):
        """Test the all command for Review."""
        self.console.onecmd("create Review")
        self.console.onecmd("create Review")
        self.console.onecmd("Review.all()")
        output = mock_stdout.getvalue().strip()
        self.assertIn("Review", output)
        self.assertIn("2", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_all_user(self, mock_stdout):
        """Test the all command for User."""
        self.console.onecmd("create User")
        self.console.onecmd("create User")
        self.console.onecmd("User.all()")
        output = mock_stdout.getvalue().strip()
        self.assertIn("User", output)
        self.assertIn("2", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_all_place(self, mock_stdout):
        """Test the all command for Place."""
        self.console.onecmd("create Place")
        self.console.onecmd("create Place")
        self.console.onecmd("Place.all()")
        output = mock_stdout.getvalue().strip()
        self.assertIn("Place", output)
        self.assertIn("2", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_all_amenity(self, mock_stdout):
        """Test the all command for Amenity."""
        self.console.onecmd("create Amenity")
        self.console.onecmd("create Amenity")
        self.console.onecmd("Amenity.all()")
        output = mock_stdout.getvalue().strip()
        self.assertIn("Amenity", output)
        self.assertIn("2", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_all_state(self, mock_stdout):
        """Test the all command for State."""
        self.console.onecmd("create State")
        self.console.onecmd("create State")
        self.console.onecmd("State.all()")
        output = mock_stdout.getvalue().strip()
        self.assertIn("State", output)
        self.assertIn("2", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_all_city(self, mock_stdout):
        """Test the all command for City."""
        self.console.onecmd("create City")
        self.console.onecmd("create City")
        self.console.onecmd("City.all()")
        output = mock_stdout.getvalue().strip()
        self.assertIn("City", output)
        self.assertIn("2", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_all_place(self):
        """Test the all command for Place."""
        self.console.onecmd("create Place")
        self.console.onecmd("create Place")
        self.console.onecmd("Place.all()")
        output = mock_stdout.getvalue().strip()
        self.assertIn("Place", output)
        self.assertIn("2", output)

if __name__ == "__main__":
    unittest.main()
