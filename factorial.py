#!/usr/bin/python

#calculates the factorial of a number

def factorial(number):
	if (number > 0) :
		total = 1
		while (number > 1) :
			total *= number
			number -= 2
		return total
	else:
		print("that is an invalid input")
		return 0
