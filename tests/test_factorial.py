import pytest

from factorial import *

def test_factorial_1():
	assert(calc_factorial(1) == 1)

def test_factorial_2():
	assert(calc_factorial(2) == 2)

def test_factorial_3():
	assert(calc_factorial(3) == 6)

def test_factorial_6():
	assert(calc_factorial(6) == 720)

def test_sieve_10():
	assert(is_prime(10) == False)

def test_sieve_11():
	assert(is_prime(11) == True)
