"""
*** Task 7 ***
Ну і традиційно -> калькулятор :) повинна бути 1 ф-цiя яка б приймала 3 аргументи - один з яких операцiя, яку зробити!
"""

def the_calculator(num_1, num_2, op):
	if op == "+":
		res = num_1 + num_2
	elif op == "-":
		res = num_1 - num_2
	elif op == "*":
		res = num_1 * num_2
	elif op == "/":
		res = num_1 / num_2
	elif op == "**":
		res = num_1 ** num_2
	else:
		res = "Sorry I do not know this operation"

	return res


num_1 = float(input("First number: "))
num_2 = float(input("Second number: "))
op = input("Operation: ")

print(the_calculator(num_1, num_2, op))
