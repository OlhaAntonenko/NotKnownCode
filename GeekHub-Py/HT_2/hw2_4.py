"""
*** Task 4 ***
Створiть 3 рiзних функцiї (на ваш вибiр). 
Кожна з цих функцiй повинна повертати якийсь результат. 
Також створiть четверу ф-цiю, яка в тiлi викликає 3 попереднi, обробляє повернутий ними результат та також повертає результат. 
Таким чином ми будемо викликати 1 функцiю, а вона в своєму тiлi ще 3
"""

def get_unique_items(items: list) -> list:
	return list(set(items))

def get_items_without_only_digits(items: list) -> list:
	return [i for i in items if not i.isdigit()]

def get_without_empty_items(items: list) -> list:
	return list(filter(None, items))

def normilaze_items(input_items: list)-> list:
	items = get_unique_items(input_items)
	items = get_items_without_only_digits(items)
	items = get_without_empty_items(items)

	return sorted(items)


checked_items = ['Abc', '2', '', 'Abc', 'def', '2.5', 'abc']
print(normilaze_items(checked_items))
