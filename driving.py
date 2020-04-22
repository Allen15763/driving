# driving
country = input('Where are you from?: ')
age = input('type your age: ')
age = int(age)
if country == 'Taiwan':
	if age >= 18:
		print('You can drive')
	else:
		print("You can't drive")

elif country == 'US':
	if age >=16:
		print('You can drive')
	else:
		print("You can't drive")
else:
	print('Please type Taiwan or US only')