"""
*** Task 1 ***
Програма-банкомат.
   Створити програму з наступним функціоналом:
      - підтримка 3-4 користувачів, які валідуються парою ім'я/пароль (файл <users.data>);
      - кожен з користувачів має свій поточний баланс (файл <{username}_balance.data>) та історію транзакцій (файл <{username}_transactions.data>);
      - є можливість як вносити гроші, так і знімати їх. Обов'язкова перевірка введених даних (введено число; знімається не більше, ніж є на рахунку).
   Особливості реалізації:
      - файл з балансом - оновлюється кожен раз при зміні балансу (містить просто цифру з балансом);
      - файл - транзакціями - кожна транзакція у вигляді JSON рядка додається в кінець файла;
      - файл з користувачами: тільки читається. Якщо захочете реалізувати функціонал додавання нового користувача - не стримуйте себе :)
   Особливості функціонала:
      - за кожен функціонал відповідає окрема функція;
      - основна функція - <start()> - буде в собі містити весь workflow банкомата:
      - спочатку - логін користувача - програма запитує ім'я/пароль. Якщо вони неправильні - вивести повідомлення про це і закінчити роботу (хочете - зробіть 3 спроби, а потім вже закінчити роботу - все на ентузіазмі :) )
      - потім - елементарне меню типа:
        Введіть дію:
           1. Продивитись баланс
           2. Поповнити баланс
           3. Вихід
      - далі - фантазія і креатив :)

"""
import datetime
import json


def check_user(username, password):
	with open('users.data.json') as f:
		data_login_data = json.load(f)
	for user in data_login_data:
		if user['name'] == username and user['password'] == password:
			return True
	return False


def view_balance(name):
	with open(f'{name}_balance.data.json', 'r') as f:
		data = json.load(f)
		print(f'Balance: {data}')
	return


def add_info_to_json_file(data, file):
	with open(file) as f:
		transactions = json.load(f)

	date_time = datetime.datetime.today().replace(microsecond=0)
	data = f"{date_time}  |  {data}"
	transactions.append(data)

	with open(file, 'w') as f:
		json.dump(transactions, f)


def change_balance(name, raise_balance=True):
	try:
		changes = int(input("Enter the amount: "))
	except ValueError:
		print('Incorrect number')
		return

	balance_file = f'{name}_balance.data.json'
	with open(balance_file) as f:
		balance = int(json.load(f))

	if raise_balance:
		action = 'Increased by'
		balance += changes
	else:
		if changes > balance:
			print('Decreased by')
			return
		action = 'Withdrawn'
		balance -= changes

	with open(balance_file, 'w') as f:
		json.dump(balance, f)

	add_info_to_json_file(f"{action}: {changes}. Balance: {balance}", f'{name}_transactions.data.json')

	return


def show_history(name):
	with open(f'{name}_transactions.data.json') as f:
		transactions = json.load(f)
	print('\n'.join(transactions))

	return


def start():
	print('Hello!')
	try_counter = 3
	while try_counter:
		username = input('Please, enter your username: ')
		password = input('Password: ')
		valid_user = check_user(username, password)

		if not valid_user:
			try_counter -= 1
			if try_counter == 0:
				print('Process canceled')
				return
			print(f"Your data is not valid. {try_counter} attempts left")
			continue

		break

	while True:
		print('Select an action:')
		print('1. View balance')
		print('2. Top up balance')
		print('3. Withdraw cash')
		print('4. History')
		print('5. Finish')

		action = int(input())

		if action == 1:
			view_balance(username)
		elif action == 2:
			change_balance(username, raise_balance=True)
		elif action == 3:
			change_balance(username, raise_balance=False)
		elif action == 4:
			show_history(username)
		elif action == 5:
			break
		print('--------------------')


start()