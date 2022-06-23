

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
