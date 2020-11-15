"""
*** Task 5 ***
Написати функцію < fibonacci >, яка приймає один аргумент і виводить всі числа Фібоначчі, що не перевищують його.
"""

def fib(n):
	fib_list = []
	a = b = 1

	while a <= n:
		fib_list.append(a)
		a, b = b, a + b
	return fib_list


print(fib(20))
