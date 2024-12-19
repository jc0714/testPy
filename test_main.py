# test_main.py
from main import greet

def test_greet():
    assert greet("World") == "Hello, World!"
    assert greet("macOS") == "Hello, macOS!"
