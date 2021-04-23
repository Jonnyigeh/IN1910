import numpy as np
import calculator
import math as m
from calculator import add, factorial, sin, divide, square, cube
"""
Exercise 1
"""
def test_add_int_exercise_1():
	x = 1
	y = 2
	assert add(x,y) == 3

def test_add_float_exercise_2():
	"""
	When using float numbers we check for equality by
	checking if the absolute value of the
	difference is below a chosen tolerance
	"""
	tol = 1e-10
	a = 0.1
	b = 0.2
	assert abs(add(a, b) - 0.3) < tol

def test_add_strings_exercise_3():
	"""
	Checking that strings are added
	like expected
	"""
	a = "hello"
	b = " world"
	assert add(a,b) == "hello world"
"""
Exercise 4
"""
def test_factorial_exercise_4():
	assert factorial(5) == m.factorial(5)
def test_sin_exercise_4():
	tol = 1e-10
	assert abs(m.sin(0) - sin(0, 20)) < tol
def test_divide_exercise_4():
	tol = 1e-10
	a = 4
	b = 2
	assert abs(divide(4, 2) - 2) < tol
def test_square_exercise_4():
	assert square(2) == 4
def test_cube_exercise_4():
	assert cube(2) == 8
"""
Exercise 5
"""
import pytest

def test_divide_zero_division_exercise_5():
	with pytest.raises(ZeroDivisionError):
		divide(5,0)
def test_add_type_error_exercise_5():
	with pytest.raises(TypeError):
		add(5, "hello")
"""
Exercise 6
Here we have the same testfunctions from task 1-4, but rewritten
on parametrized form as specified in exercise 6.
Did not include the last two testfunctions, as i didnt see
any reason to test for more than one type of error.
"""
@pytest.mark.parametrize("arg, eo", [[(1, 1), 2],[(2, 2), 4], [(3, 5), 8]])
def test_add_exercise_6(arg, eo):
	"""
	When using float numbers we check for equality by
	checking if the absolute value of the
	difference is below a chosen tolerance
	"""
	tol = 1e-10
	assert abs(add(arg[0], arg[1]) - eo) < tol

@pytest.mark.parametrize("x", [2, 3, 4])
def test_factorial_exercise_6(x):
	assert factorial(x) == m.factorial(x)

@pytest.mark.parametrize("x", [0, np.pi, 2*np.pi])
def test_sin_exercise_6(x):
	tol = 1e-10
	assert abs(m.sin(x) - sin(x, 20)) < tol

@pytest.mark.parametrize("arg, eo", [[(2, 2), 1], [(4, 2), 2], [(9,3), 3]])
def test_divide_exercise_6(arg, eo):
	tol = 1e-10
	assert abs(divide(arg[0], arg[1]) - eo) < tol

@pytest.mark.parametrize("arg, eo", [[2, 4], [3, 9]])
def test_square_exercise_6(arg, eo):
	assert square(arg) == eo

@pytest.mark.parametrize("arg, eo", [(2, 8), (3, 27), (5, 125)])
def test_cube_exercise_6(arg, eo):
	assert cube(arg) == eo
