"""
*** Task 6 ***
Маємо рядок --> "f98neroi4nr0c3n30irn03ien3c0rfekdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p465jnpoj35po6j345" -> просто потицяв по клавi
   Створіть ф-цiю, яка буде отримувати рядки на зразок цього, яка оброблює наступні випадки:
-  якщо довжина рядка в діапазонi 30-50 -> прiнтує довжину, кiлькiсть букв та цифр
-  якщо довжина менше 30 -> прiнтує суму всiх чисел та окремо рядок без цифр (лише з буквами)
-  якщо довжина бульше 50 - > ваша фантазiя
"""

def check_str(text: str) -> str:
	length = len(text)
	only_letters, only_numbers = [], []
	for i in text:
		if i.isalpha():
			only_letters.append(i)
		elif i.isdigit():
			only_numbers.append(int(i))


	if 30 <= length <= 50:
		res = f"Len: {length}\nCount of letters: {len(only_letters)}\nCount of numbers: {len(only_numbers)}"
	elif length < 30:
		res = f"Sum of numbers: {sum(only_numbers)}\nWithout numbers: {''.join(only_letters)}"
	else:
		freq_map = {}
		for i in text:
			freq = text.count(i)
			if freq not in freq_map:
				freq_map[freq] = {i}
			else:
				freq_map[freq].add(i)

		res = "hmmm, a lot of symbols."
		if freq_map:
			max_freq = max(freq_map.keys())
			res += f"\nI think your favorite symbols: {freq_map[max_freq]}"

	return res


print(check_str(input("String: ")))
