"""
*** Task 8 ***
Write a script to replace last value of tuples in a list.
		Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
		Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
"""

main_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
val = 100
index = -1

new_list = []
for item in main_list:
	item = list(item)
	item[index] = val
	new_list.append(tuple(item))

print(new_list)
