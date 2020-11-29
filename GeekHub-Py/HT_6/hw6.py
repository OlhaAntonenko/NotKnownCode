"""
Cash machine
"""
import datetime
import json
from pathlib import Path


class CashMachine:
    data_root_path = Path('data')
    banknotes_path = data_root_path / 'banknotes.json'
    users_data_path = data_root_path / 'users.data.json'
    balance_suffix_path = '_balance.data.json'
    transactions_suffix_path = '_transactions.data.json'

    def __init__(self):
        self.users_data = load_json_data(self.users_data_path)

    def __call__(self):
        print('Welcome!')
        username = self.users_verification()
        if username == 'Admin':
            self.admin_mode()
        elif username:
            self.user_mode(username)

    def admin_mode(self):
        while True:
            print('Select an action:')
            print('1. View available banknotes')
            print('2. Load banknotes')
            print('3. Finish')

            action = int(input())

            if action == 1:
                self.view_available_banknotes()
            elif action == 2:
                self.load_banknotes()
            elif action == 3:
                break
            print('--------------------')

    def user_mode(self, username):
        while True:
            print('Select an action:')
            print('1. View balance')
            print('2. Top up balance')
            print('3. Withdraw cash')
            print('4. History')
            print('5. Finish')

            action = int(input())

            if action == 1:
                self.view_balance(username)
            elif action == 2:
                self.raise_balance(username)
            elif action == 3:
                self.withdraw(username)
            elif action == 4:
                self.show_history(username)
            elif action == 5:
                break
            print('--------------------')

    def users_verification(self):
        try_counter = 3
        while try_counter:
            username = input('Please, enter your username: ')
            password = input('Password: ')
            valid_user = self.check_user(username, password)

            if valid_user:
                return username
            else:
                try_counter -= 1
                if try_counter == 0:
                    print('Process canceled')
                    return

                print(f"Your data is not valid. {try_counter} attempts left")
                continue

    def check_user(self, username: str, password: str) -> bool:
        for user in self.users_data:
            if (user['name'], user['password']) == (username, password):
                return True
        return False

    def view_balance(self, name):
        balance_file = name + self.balance_suffix_path
        data = load_json_data(self.data_root_path / balance_file)
        print(f'Balance: {data}')

    def raise_balance(self, name):
        try:
            changes = int(input("Enter the amount: "))
        except ValueError:
            print('Incorrect number')
            return

        balance_file = self.data_root_path / (name + self.balance_suffix_path)
        balance = load_json_data(balance_file)
        balance += changes
        dump_json_data(balance, balance_file)

        transaction_file = name + self.transactions_suffix_path
        self.add_info_to_json_file(f"Increased by: {changes}. Balance: {balance}",
                                   self.data_root_path / transaction_file)

    def withdraw(self, name):
        try:
            changes = int(input("Enter the amount: "))
        except ValueError:
            print('Incorrect number')
            return

        balance_file = self.data_root_path / (name + self.balance_suffix_path)
        balance = int(load_json_data(balance_file))

        if changes > balance:
            print('Not enough money for withdraw')
            return

        banknotes = self.get_cash_withdrawal(changes)
        if not banknotes:
            print('Problems during withdrawal')
            return

        balance -= changes
        dump_json_data(balance, balance_file)
        transaction_file = name + self.transactions_suffix_path
        self.add_info_to_json_file(f"Decreased by: {changes}. Balance: {balance}",
                                   self.data_root_path / transaction_file)

        print(f'Banknotes:')
        for nom, count in banknotes:
            print(f'Nominal: {nom}, count: {count}')

    @staticmethod
    def add_info_to_json_file(data, file):
        transactions = load_json_data(file)

        date_time = datetime.datetime.today().replace(microsecond=0)
        transactions.append(f"{date_time}  |  {data}")

        dump_json_data(transactions, file)

    def show_history(self, name):
        transactions_file = name + self.transactions_suffix_path
        print('\n'.join(load_json_data(self.data_root_path / transactions_file)))

    def view_available_banknotes(self):
        print(load_json_data(self.banknotes_path))

    def load_banknotes(self):
        print('Enter `DONE` for finish')
        banknotes = {int(k): v for k, v in load_json_data(self.banknotes_path).items()}

        while True:
            try:
                users_input = input("Nominal and count (use space between them): ")
                if users_input.casefold() == 'done':
                    dump_json_data({str(k): v for k, v in banknotes.items()}, self.banknotes_path)
                    return

                nom, count = map(int, users_input.split())

                if nom in banknotes:
                    banknotes[nom] += count
                else:
                    banknotes[nom] = count
            except ValueError:
                print('Incorrect data')

    def get_cash_withdrawal(self, needed_cash):
        banknotes = {int(k): v for k, v in load_json_data(self.banknotes_path).items()}
        result = []

        all_cash = sorted(banknotes, reverse=True)
        current_n = needed_cash

        for i, nom in enumerate(all_cash):
            if not current_n:
                break

            div = current_n // nom
            if 0 < div <= banknotes[nom]:
                check_n = current_n - div * nom
                if [g for g in all_cash[i:] if check_n % g == 0]:
                    current_n = check_n
                    result.append((nom, div))

        if current_n:
            return

        for nom, count in result:
            banknotes[nom] -= count
            if banknotes[nom] == 0:
                banknotes.pop(nom)

        dump_json_data({str(k): v for k, v in banknotes.items()}, self.banknotes_path)
        return result


def load_json_data(path: str):
    with open(path) as f:
        return json.load(f)


def dump_json_data(data, path: str):
    with open(path, 'w') as f:
        json.dump(data, f)


if __name__ == '__main__':
    cash_class = CashMachine()
    while True:
        cash_class()
