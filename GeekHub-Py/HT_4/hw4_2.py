"""
*** Task 2 ***
Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
   - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
   - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну цифру;
   - щось своє :)
   Якщо якийсь із параментів не відповідає вимогам - породити виключення із відповідним текстом.
"""

import re


class SigninException(Exception):
	def __init__(self, text):
		self.text = text


def check_data(username, password):
	try:
		name_len = len(username)
		if name_len < 3:
			raise SigninException('Length of name should be more than 3 symbols')
		elif name_len > 50:
			raise SigninException('Length of name should be less than 50 symbols')
		elif len(password) < 8:
			raise SigninException('Length of password should not be less than 8 symbols')
		elif not re.search(r'\d', password):
			raise SigninException('Password should contain at least one digit')
		elif password.casefold() in ['qwerty1234', '00000000', '123456789']:
			raise SigninException('Easy password. Please change it to more secure.')
	except SigninException as err:
		return err.text
	else:
		return True


print(check_data('Vasya', '00000000'))
