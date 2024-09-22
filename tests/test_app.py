# tests/test_app.py

import app  # Import your app.py module

def test_add_two_numbers():
    assert app.add(2, 3) == 5

def test_add_multiple_numbers():
    assert app.add(1, 2, 3, 4) == 10

# Add more test cases for various scenarios (edge cases, negative numbers, etc.)