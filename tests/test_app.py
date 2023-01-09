"""
Test module for app

Classes: TestApp()
"""
from autotest.tests import myapp_env
from app import app

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
        print(myapp_env.sys)
        assert True

    def test_two(self):
        """Test two"""
        assert app.run()
