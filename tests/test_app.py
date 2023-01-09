"""
Test module for app

Classes: TestApp()
"""
import pytest
import main

# content of test_class_demo.py
class TestApp:
    def test_one(self):
        """Test one"""
        assert True

    def test_two(self):
        """Test two"""
        assert main.app()
