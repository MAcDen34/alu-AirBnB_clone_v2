#!/usr/bin/python3
"""Unittest for DBStorage engine"""
import unittest
import os


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
                 "Only for DB storage")
class TestDBStorage(unittest.TestCase):
    """Tests for DBStorage"""

    def test_all_returns_dict(self):
        """Test that all returns a dictionary"""
        from models import storage
        self.assertIsInstance(storage.all(), dict)

    def test_new_and_save(self):
        """Test that new and save work"""
        from models import storage
        from models.state import State
        s = State(name="TestState")
        storage.new(s)
        storage.save()
        key = "State.{}".format(s.id)
        self.assertIn(key, storage.all())

    def test_delete(self):
        """Test that delete works"""
        from models import storage
        from models.state import State
        s = State(name="DeleteMe")
        storage.new(s)
        storage.save()
        storage.delete(s)
        storage.save()
        key = "State.{}".format(s.id)
        self.assertNotIn(key, storage.all())

    def test_reload(self):
        """Test that reload works"""
        from models import storage
        try:
            storage.reload()
        except Exception as e:
            self.fail("reload() raised exception: {}".format(e))

    def test_close(self):
        """Test that close works"""
        from models import storage
        try:
            storage.close()
        except Exception as e:
            self.fail("close() raised exception: {}".format(e))


if __name__ == "__main__":
    unittest.main()
