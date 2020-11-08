"""
*** Task 6 ***
Write a script to check whether a specified value is contained in a group of values.
		Test Data :
		3 -> [1, 5, 8, 3] : True
		-1 -> (1, 5, 8, 3) : False
"""

val = int(input("Specified value: "))
group = map(float, input("Group of values: ").split(","))
print(val in group)
