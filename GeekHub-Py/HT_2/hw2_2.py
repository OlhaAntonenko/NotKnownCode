"""
*** Task 2 ***
Користувачем вводиться початковий і кінцевий рік. Створити цикл, який виведе всі високосні роки в цьому проміжку (границі включно).
"""

year_from = int(input("From: "))
year_to = int(input("To: "))

for year in range(year_from, year_to + 1):
	if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
		print(year)
