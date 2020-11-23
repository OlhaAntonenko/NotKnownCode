"""
*** Task 3 ***
Написати функцію, яка приймає два параметри: ім'я файлу та кількість символів.
   На екран повинен вивестись список із трьома блоками - символи з початку, із середини та з кінця файлу.
   Кількість символів в блоках - та, яка введена в другому параметрі.
   Придумайте самі, як обробляти помилку, наприклад, коли кількість символів більша, ніж є в файлі 
   (наприклад, файл із двох символів і треба вивести по одному символу, то що виводити на місці середнього блоку символів?)
"""

def get_blocks(file, count=1):
	with open(file, 'r') as f:
		data = f.read()

	total_lenght = len(data)

	if 3 * count <= total_lenght:
		start = data[:count]

		middle_index = total_lenght // 2
		if total_lenght % 2 != 0:
			if count % 2 != 0:
				left_offset = middle_index - count // 2
				right_offset = middle_index + count // 2 + 1
				middle = data[left_offset:right_offset]
			else:
				count -= 1
				left_offset = middle_index - count // 2
				right_offset = middle_index + count // 2 + 1
				middle = data[left_offset:right_offset + 1]

		else:
			left_offset = middle_index - count // 2
			middle = data[left_offset:left_offset+count]

		end = data[-count:]


	elif 2 * count <= total_lenght:
		start = data[:count]
		middle = ''
		end = data[-count:]
	else:
		start = data[:count] if count <= total_lenght else ''
		middle, end = '', ''

	ret = [start, middle, end]
	
	return data, ret


symbol_count = 4
data, blocks = get_blocks('text.txt', symbol_count)

print(f'Data: {data}, symbol_count: {symbol_count}, blocks: {blocks}')
