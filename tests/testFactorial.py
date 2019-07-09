import pytest

from factorial.factorial import factorial

def test_factorial_6():
	assert(factorial(6) == 720)

def test_factorial_8():
	assert(factorial(8) == 40320

def test_factorial_10():
	assert(factorial(10) == 3628800)
