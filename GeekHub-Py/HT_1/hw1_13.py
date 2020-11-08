"""
*** Task 13***
Write a script to get the maximum and minimum value in a dictionary.
"""

dict_data = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

values = dict_data.values()
print(f"Min: {min(values)}, Max: {max(values)}")
