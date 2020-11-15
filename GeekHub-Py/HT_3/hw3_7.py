"""
*** Task 7 ***
Написати функцію, яка приймає на вхід список і підраховує кількість однакових елементів у ньому.
"""

from collections import Counter


def get_count_of_elem(x: list):
	return dict(Counter(x))


print(f'Count of elements: {get_count_of_elem([0, 0, 1, 2, 3, 1, 2, 3, 4])}')
