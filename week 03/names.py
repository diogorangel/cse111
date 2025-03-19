# Copyright 2020, Brigham Young University-Idaho. All rights reserved.
from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    """Test the make_full_name function with various name formats."""
    assert make_full_name("John", "Doe") == "Doe; John"
    assert make_full_name("Anna", "Smith") == "Smith; Anna"
    assert make_full_name("Mary-Jane", "O'Connor") == "O'Connor; Mary-Jane"
    assert make_full_name("A", "B") == "B; A"
    assert make_full_name("Jean-Luc", "Picard") == "Picard; Jean-Luc"


def test_extract_family_name():
    """Test the extract_family_name function with different full names."""
    assert extract_family_name("Doe; John") == "Doe"
    assert extract_family_name("Smith; Anna") == "Smith"
    assert extract_family_name("O'Connor; Mary-Jane") == "O'Connor"
    assert extract_family_name("B; A") == "B"
    assert extract_family_name("Picard; Jean-Luc") == "Picard"

    # Extract a substring from the full name and return it.


def test_extract_given_name():
    assert extract_given_name("John Doe") == "John"
    assert extract_given_name("Anna Smith") == "Anna"
    assert extract_given_name("Mary-Jane O'Connor") == "Mary-Jane"
    assert extract_given_name("A B") == "A"

pytest.main(["-v", "--tb=line", "-rN", __file__])