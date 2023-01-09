"""
This module imports dependencies for test apps

"""
import sys

sys.path.append("../")

def module_app():
    """Module to invoke an app module."""
    import app
    return app
