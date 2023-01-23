import pytest
from pow import *

def test_pow_number():
    assert pow(5) == 25

def test_pow_number_str():
    assert pow("5") == 25

def test_pow_negative_number_str():
    assert pow("-5") == 25

def test_pow_letter():
    with pytest.raises(ValueError):
        assert pow("a")