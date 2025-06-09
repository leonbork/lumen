"""
This file stores test data, including user credentials for various scenarios.
"""

class TestData:
    """
    Class to hold various test data.
    """
    VALID_USER = {
        "email": "test@lumen.me",
        "password": "qwerty"
    }

    INVALID_USER = {
        "email": "wrong@lumen.me",
        "password": "wrongpassword"
    }

    ANOTHER_INVALID_USER = {
        "email": "another@invalid.com",
        "password": "badpass"
    }

    EMPTY_USER = {
        "email": "",
        "password": ""
    }

