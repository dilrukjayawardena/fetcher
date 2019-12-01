import sys

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class ValueNotValidForFieldError(Error):
   """Raised when the input value is too large"""
   pass