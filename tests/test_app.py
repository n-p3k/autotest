"""
Test module for app

Classes: TestApp()
"""
import sys
sys.path.append("../")

import app

# content of test_class_demo.py
class TestApp:
    """
    A class to test the app.

    Methods
    -------
    test_one():
        First test.
     test_two():
        Second test.
    """
    def test_one(self):
        """Test one"""
        assert True

    def test_two(self):
        """Test two"""
        assert app.app()
