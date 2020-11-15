"""
*** Task 6 ***
Вводиться число. Якщо це число додатне, знайти його квадрат, якщо від'ємне, збільшити його на 100, якщо дорівнює 0, не змінювати.
"""

def check_value(n):
	if n > 0:
		ret = n ** 2
	elif n < 0:
		ret = n + 100
	else:
		ret = n

	return ret


print(check_value(20))
