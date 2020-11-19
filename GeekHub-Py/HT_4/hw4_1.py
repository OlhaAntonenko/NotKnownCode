"""
*** Task 1 ***
Створіть функцію, всередині якої будуть записано список із п'яти користувачів (ім'я та пароль).
   Функція повинна приймати три аргументи: 
   два - обов'язкових (<username> та <password>) і третій - необов'язковий параметр <silent> (значення за замовчуванням - <False>).
   Логіка наступна:
       якщо введено коректну пару ім'я/пароль - вертається <True>;
       якщо введено неправильну пару ім'я/пароль і <silent> == <True> - функція вертає <False>, 
       інакше (<silent> == <False>) - породжується виключення LoginException
"""

class LoginException(Exception):
	def __init__(self, text):
		self.text = text


def users_data(username, password, silent=False):
	users_db = [
		{'Vasya': '1234'},
		{'Kolya': '5678'},
		{'Tolya': 'qwerty'},
		{'Petya': '0000'},
		{'Katya': '1111'}
	]
	try:
		if {username: password} in users_db:
			return True
		elif silent:
			return False
		else:
			raise LoginException("Incorrect login data")
	except LoginException as err:
		return err.text


print(users_data('Vasya', '123'))
