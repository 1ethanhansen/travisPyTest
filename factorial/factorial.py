#!/usr/bin/python

#calculates the factorial of a number

def calc_factorial(number):
	if (number > 0) :
		total = 1
		while (number > 1) :
			total *= number
			number -= 1
		return total
	else:
		print("that is an invalid input")
		return 0

def is_prime(number):
	prime = [True for i in range(number+1)]
	p = 2
	while (p * p <= number):
		if (prime[p] == False):
			p += 1
			continue

		for i in range(p * 2, number+1, p):
			if (i == number):
				return False
			prime[i] = False
		p += 1

	return True
