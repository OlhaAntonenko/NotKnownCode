"""
*** Task 5 ***
Користувач вводить змiннi "x" та "y" з довiльними цифровими значеннями;
-  Створiть просту умовну конструкцiю(звiсно вона повинна бути в тiлi ф-цiї), 
	пiд час виконання якої буде перевiрятися рiвнiсть змiнних "x" та "y" 
	і при нерiвностi змiнних "х" та "у" вiдповiдь повертали рiзницю чисел.
-  Повиннi опрацювати такi умови:
-  x > y;       вiдповiдь - х бiльше нiж у на z
-  x < y;       вiдповiдь - у бiльше нiж х на z
-  x == y.      вiдповiдь - х дорiвнює z
"""

def check_two_numbers(x: int, y: int) -> str:
	if x > y:
		res = f"x is greater than y on {x - y}"
	elif x < y:
		res = f"y is greater than x on {y - x}"
	else:
		res = "х and y are equal"

	return res


x, y = int(input("x = ")), int(input("y = "))
print(check_two_numbers(x, y))
