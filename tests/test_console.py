#!/usr/bin/python3
"""
test module
"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    @patch('sys.stdout', new_callable=StringIO)
    def test_help_show(self, mock_stdout):
        with patch('sys.stdin', return_value='EOF'):
            self.console.onecmd("help show")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "Output the string representation of an object using its class name and ID")

    def test_do_EOF(self):
        with patch('sys.stdin', return_value='EOF'):
            result = self.console.onecmd("EOF")
            self.assertTrue(result)

    def test_do_quit(self):
        result = self.console.onecmd("quit")
        self.assertTrue(result)

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_create(self, mock_stdout):
        with patch('sys.stdin', return_value='EOF'):
            self.console.onecmd("create BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_show(self, mock_stdout):
        with patch('sys.stdin', return_value='EOF'):
            self.console.onecmd("show BaseModel 123")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_destroy(self, mock_stdout):
        with patch('sys.stdin', return_value='EOF'):
            self.console.onecmd("destroy BaseModel 123")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_all(self, mock_stdout):
        with patch('sys.stdin', return_value='EOF'):
            self.console.onecmd("all")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_update(self, mock_stdout):
        with patch('sys.stdin', return_value='EOF'):
            self.console.onecmd("update BaseModel 123 attribute value")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_count(self, mock_stdout):
        with patch('sys.stdin', return_value='EOF'):
            self.console.onecmd("count BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_default(self, mock_stdout):
        with patch('sys.stdin', return_value='EOF'):
            self.console.onecmd("UnknownSyntax")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(output)


if __name__ == '__main__':
    unittest.main()
