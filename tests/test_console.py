#!/usr/bin/python3
"""Unittest for console.py"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Tests for the HBNB console"""

    def test_prompt(self):
        """Test prompt is correct"""
        self.assertIn(HBNBCommand.prompt, ["(hbnb) ", ""])

    def test_empty_line(self):
        """Test empty line does nothing"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("")
            self.assertEqual("", f.getvalue())

    def test_quit(self):
        """Test quit command"""
        with self.assertRaises(SystemExit):
            HBNBCommand().onecmd("quit")

    def test_help(self):
        """Test help command exists"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            self.assertIn("Documented commands", f.getvalue())

    def test_show_no_args(self):
        """Test show with no args"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            self.assertIn("** class name missing **", f.getvalue())

    def test_create_no_args(self):
        """Test create with no args"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertIn("** class name missing **", f.getvalue())

    def test_destroy_no_args(self):
        """Test destroy with no args"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            self.assertIn("** class name missing **", f.getvalue())

    def test_all_no_args(self):
        """Test all with no args"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
            self.assertIsNotNone(f.getvalue())

    def test_update_no_args(self):
        """Test update with no args"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
            self.assertIn("** class name missing **", f.getvalue())

    def test_invalid_class(self):
        """Test show with invalid class"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show MyModel")
            self.assertIn("** class doesn't exist **", f.getvalue())


if __name__ == "__main__":
    unittest.main()
