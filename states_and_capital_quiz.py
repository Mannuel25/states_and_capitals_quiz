import random

def capitalQuiz():
	states_capital = {
		'Abia':'Umuahia',
		'Adamawa':'Yola',
		'Akwa Ibom':'Uyo',
		'Anambra' : 'Awka',
		'Bauchi':'Bauchi',
		'Bayelsa':'Yenegoa',
		'Benue':'Makurdi',
		'Bornu':'Maiduguri',
		'Cross River':'Calabar',
		'Delta':'Asaba',
		'Ebonyi':'Abakaliki',
		'Edo':'Benin',
		'Enugu':'Enugu',
		'Ekiti':'Ado Ekiti',
		'Gombe':'Gombe',
		'Imo':'Owerri',
		'Jigawa':'Dutse',
		'Kaduna':'Kaduna',
		'Kano':'Kano',
		'Katsina':'Katsina',
		'Kogi':'Lokoja',
		'Kwara':'Ilorin',
		'Kebbi':'Benin Kebbi',
		'Lagos':'Ikeja',
		'Nassarawa':'Lafia',
		'Niger':'Mina',
		'Ogun':'Abeokuta',
		'Ondo':'Akure',
		'Osun':'Osogbo',
		'Oyo':'Ibadan',
		'Plateau':'Jos',
		'Rivers':'Port Harcourt',
		'Sokoto':'Sokoto',
		'Taraba':'Jalingo',
		'Yobe':'Damaturu',
		'Zamfara':'Gusau',
		}
	correct_guess = 0
	incorrect_guess = 0
	no_of_guess = 0
	print('\t\tStates and capital quiz')
	print('+ Enter Yes to start quiz')
	print('+ Enter No to end quiz')
	print('+ Enter scoreboard to display scores')
	print('+ Enter states and capitals to display the full list')
	menu = ['NO','No','YES','Yes','SCOREBOARD','Scoreboard','States And Capitals','STATES AND CAPITALS']
	play = input('\nStart quiz?: ')
	if play.title() not in menu:
		print('Invalid choice!')
	else:	
		while play.title() != 'No' or play.title() == 'NO':
			if play.title() == 'States And Capitals'or play.title() == 'STATES AND CAPITALS':
				index = 1
				for key,value in states_capital.items():
					print(f'\n{index}. {key} : {value}') 
					index += 1
			elif play.title() == 'SCOREBOARD' or play.title() == 'Scoreboard':
				pass_accuracy = (correct_guess / no_of_guess) * 100
				print(f'\nNumber of guesses: {no_of_guess}')
				print(f'Correct guesses: {correct_guess}')
				print(f'Incorrect guesses: {incorrect_guess}')
				print('Pass accuracy: {:.2f}%'.format(pass_accuracy))
			elif play.title() == 'Yes' or play.title() == 'YES':	
				states = [i for i in states_capital]
				random_state = ''.join(random.sample(states,1))
				capital = input(f'Enter the capital for {random_state} state: ')
				no_of_guess += 1
				if states_capital[random_state] == capital.title():
					print('Bravo!... 😉')
					correct_guess += 1
				else:
						incorrect_guess += 1
						print('Wrong... 😢')
						for key,value in states_capital.items():
							if key == random_state:
								print(f'The capital for {key} state is {value}')

			play = input('\nTake quiz again?: ')

capitalQuiz()















