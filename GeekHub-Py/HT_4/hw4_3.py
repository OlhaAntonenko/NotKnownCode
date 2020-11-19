"""
*** Task 3 ***
На основі попередньої функції створити наступний кусок кода:
   а) створити список із парами ім'я/пароль різноманітних видів (орієнтуйтесь по правилам своєї функції) - як валідні, так і ні;
   б) створити цикл, який пройдеться по цьому списку і, користуючись валідатором, перевірить ці дані і надрукує для кожної пари значень відповідне повідомлення, наприклад:
      Name: vasya
      Password: wasd
      Status: password must have at least one digit
      -----
      Name: vasya
      Password: vasyapupkin2000
      Status: OK
   P.S. Не забудьте використати блок try/except ;)
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
		return 'OK'


data_list = [
	('Vasya', 'gavgav4556'),
	('dd', 'password78'),
	('MyName', 'password'),
	('SomeSome', '123456789'),
	('Just11111111111111111111111111111111111111111111111', 'dcdddddd123'),
]

for username, password in data_list:
	print(f'Name: {username}\nPassword: {password}\nStatus: {check_data(username, password)}\n-----')
