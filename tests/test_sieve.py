import pytest

from factorial.factorial import is_prime

def test_sieve_10():
        assert(is_prime(10) == False)

def test_sieve_11():
        assert(is_prime(11) == True)

