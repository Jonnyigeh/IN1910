"""
Exercise 1, 2, 3
"""
def add(x, y):
	return x + y
"""
Exercise 4
"""
import math as m
import numpy as np

def factorial(x):
	facto = 1
	for i in range(1, x+1):
		facto *= i
	return facto

def sin(x, N):
	sin = sum((-1)**N*x**(2*N+1)/factorial(2*N + 1) for N in range(N))
	return sin

def divide(x, y):
	return x/y

def cube(x):
	return x**3
def square(x):
	return x**2
