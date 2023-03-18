import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestHBNBCommand(unittest.TestCase):

<<<<<<< HEAD
=======
class TestHBNBCommand(unittest.TestCase):
    """Console Tests"""
>>>>>>> 104b64726d0190383d34774f6f421b26b516025f
    def setUp(self):
        """Reset the file storage"""
        self.cli = HBNBCommand()

    def tearDown(self):
        """Remove the file storage"""
        del self.cli

    def test_create(self):
        """Test the `create` command"""
        # Test invalid usage
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd('create')
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd('create MyModel')
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

        # Test valid usage
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd('create BaseModel')
            self.assertEqual(len(f.getvalue().strip()), 36)

    def test_show(self):
        """Test the `show` command"""
        # Test invalid usage
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd('show')
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd('show MyModel')
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd('show BaseModel')
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd('show BaseModel 12345')
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

        # Test valid usage
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd('create BaseModel')
            instance_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd(f'show BaseModel {instance_id}')
            self.assertIn(instance_id, f.getvalue())

    def test_destroy(self):
        """Test the `destroy` command"""
        # Test invalid usage
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd('destroy')
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd('destroy MyModel')
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd('destroy BaseModel')
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd('destroy BaseModel 12345')
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

        # Test valid usage
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd('create BaseModel')
            instance_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd(f'destroy BaseModel {instance_id}')
            self.assertFalse(f.getvalue().strip())
