"""
*** Task 11 ***
Write a script to remove duplicates from Dictionary.
"""

test_dict = {1:10, 2:20, 3:20, 4:40}
dict_with_unique_val = {}

for k, v in test_dict.items():
	if v not in dict_with_unique_val.values():
		dict_with_unique_val[k] = v

print(dict_with_unique_val)
