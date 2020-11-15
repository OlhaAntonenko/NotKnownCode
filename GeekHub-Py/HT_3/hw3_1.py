"""
*** Task 1 ***
Написати функцію < square > , яка прийматиме один аргумент - сторону квадрата, і вертатиме 3 значення (кортеж): 
периметр квадрата, площа квадрата та його діагональ.
"""

import math


def square(n:int):
	p_square = 4 * n
	s_square = n ** 2
	d_square = math.sqrt(2 * n ** 2)

	return p_square, s_square, d_square


print(square(2))
