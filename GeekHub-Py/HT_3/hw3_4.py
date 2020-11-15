"""
*** Task 4 ***
Написати функцію < prime_list >, яка прийматиме 2 аргументи - початок і кінець діапазона, і вертатиме список простих чисел всередині цього діапазона.
"""

def is_prime(n):
	if n < 2:
		return False

	for i in range(2, n):
		if n % i == 0:
			return False

	return True


def prime_list(start, end):
	return [i for i in range(start, end + 1) if is_prime(i)]


print(prime_list(0, 100))
