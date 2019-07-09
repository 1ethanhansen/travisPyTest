import pytest

from factorial import calc_factorial

def test_factorial_1():
	assert(calc_factorial(1) == 1)

def test_factorial_2():
	assert(calc_factorial(2) == 2)

def test_factorial_3():
	assert(calc_factorial(3) == 6)

def test_factorial_6():
	assert(calc_factorial(6) == 720)
