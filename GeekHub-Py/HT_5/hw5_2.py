"""
*** Task 2 ***
Програма-світлофор.
   Створити програму-емулятор світлофора для авто і пішоходів.
   Після запуска програми на екран виводиться в лівій половині - колір автомобільного, а в правій - пішохідного світлофора.
   Кожну секунду виводиться поточні кольори. Через декілька ітерацій - відбувається зміна кольорів - логіка така сама як і в звичайних світлофорах.
   Приблизний результат роботи наступний:
      Red        Green
      Red        Green
      Red        Green
      Red        Green
      Yellow     Green
      Yellow     Green
      Green      Red
      Green      Red
      Green      Red
      Green      Red
      Yellow     Red
      Yellow     Red
      Red        Green
      .......
"""
from time import sleep


color_timing = {
	'Red': 4,
	'Yellow': 2,
	'Green': 4
}


def traffic_light():
	while True:
		human_mapping = {
			'Red': 'Green',
			'Green': 'Red'
		}
		for car_color in ['Red', 'Yellow', 'Green', 'Yellow']:
			if car_color == 'Yellow':
				human_color = human_mapping.get(prev_color, '')
			else:
				human_color = human_mapping.get(car_color, '')

			time_counter = color_timing.get(car_color, 1)
			while time_counter:
				print(car_color.ljust(10) + human_color.ljust(10))
				sleep(1)
				time_counter -= 1

			prev_color = car_color


traffic_light()
