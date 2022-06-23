

import pytest
from prime import PrimeFactors


def test_prime_class():
    """
    Testing the class is imported and callable.
    """
    prime = PrimeFactors()
    assert prime