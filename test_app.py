from app import app


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
        assert app.run()
