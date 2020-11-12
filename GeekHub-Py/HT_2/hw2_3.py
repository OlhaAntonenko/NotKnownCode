"""
*** Task 3 ***
Написати функцiю season, яка приймає один аргумент — номер мiсяця (вiд 1 до 12), яка буде повертати пору року, 
якiй цей мiсяць належить (зима, весна, лiто або осiнь)
"""

def season(month: int) -> str:
	month_to_season = {
		(12, 1, 2): "winter",
		(3, 4, 5): "spring",
		(6, 7, 8): "summer",
		(9, 10, 11): "autumn"
	}
	for k, v in month_to_season.items():
		if month in k:
			return v
	return "Not corrent number of month"


print(season(int(input("Number of month: "))))
