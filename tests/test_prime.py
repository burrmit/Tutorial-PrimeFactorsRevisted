

import pytest
from prime import prime_factors


def test_prime_class():
    """
    Testing the class is imported and callable.
    """
    prime = prime_factors()
    assert prime

def test_prime_factor_data_type():
    """
    Test that data type is only int or raise ValueError.
    """
    with pytest.raises(ValueError):
        prime_factors('somestring')

def test_1_returns_empty_string():
    """
    Test to ensure empty string when 1 is passed to it.
    """
    assert [number for number in prime_factors(1)] == []

def test_2_returns_2():
    """
    Test that passing 2 returns 2.
    """
    assert [number for number in prime_factors(2)] == [[2]]

def test_3_returns_3():
    """
    Test that 3 returns 3.
    """
    assert [number for number in prime_factors(3)] == [[3]]
