"""
*** Task 9 ***
Write a script to remove an empty tuple(s) from a list of tuples.
		Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
		Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']
"""

main_list = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
print([i for i in main_list if i])
