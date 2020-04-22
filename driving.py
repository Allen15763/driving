# driving
country = input('Where are you from?: ')
age = input('type your age: ')
age = int(age)
if country == 'Taiwan':
	if age >= 18:
		print('You can drive')
	else:
		print("You can't drive")
