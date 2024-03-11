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


if __name__ == "__main__":
    unittest.main()
