"""
*** Task 6 ***
Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.
   P.S. Повинен вертатись генератор.
   P.P.S. Для повного розуміння цієї функції - можна почитати документацію по ній: https://docs.python.org/3/library/stdtypes.html#range
"""

def range_generator(*args, **kwargs):
	if kwargs:
		raise TypeError("range_generator() takes no keyword arguments")

	if len(args) == 3:
		start, stop, step = args
		if step == 0:
			raise ValueError("range_generator() arg 3 must not be zero")
	elif len(args) == 2:
		start, stop, step = *args, 1
	elif len(args) == 1:
		start = 0
		stop = args[0]
		step = 1
	else:
		raise TypeError(f"Range expected at most 3 arguments, got {len(args)}")



	i = 0
	while True:
		item = start + step*i
		if (step > 0 and item < stop) or (step < 0 and item > stop):
			yield item
			i += 1
		else:
			break

	return 

print(list(range_generator(4)))
