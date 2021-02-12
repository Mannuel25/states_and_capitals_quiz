import random
from STATES_AND_CAPITALS import states_capital

def main():
	correct_attempts = 0
	incorrect_attempts = 0
	no_of_attempts = 0
	print('\t\tStates and capital quiz')
	print('+ Enter Yes to start quiz')
	print('+ Enter No to end quiz')
	print('+ Enter scoreboard to display scores')
	print('+ Enter states and capitals to display the states and their capitals')
	menu = ['NO','N','YES','Y','SCOREBOARD','Scoreboard','States And Capitals','STATES AND CAPITALS']
	proceedQuiz = input('\nStart quiz?: ')
	proceedQuiz = proceedQuiz.strip().upper()
	while proceedQuiz not in menu:
		print('Invalid choice!')
		proceedQuiz = input('\nStart quiz?: ')
		proceedQuiz = proceedQuiz.strip().upper()
	else:	
		while True:
			if proceedQuiz == 'N' or proceedQuiz == 'NO': break
			if proceedQuiz == 'States And Capitals'or proceedQuiz == 'STATES AND CAPITALS':
				index = 1
				for key,value in states_capital.items():
					print(f'\n{index}. {key} : {value}') 
					index += 1
			if proceedQuiz == 'SCOREBOARD' or proceedQuiz == 'Scoreboard':
				pass_accuracy = (correct_attempts / no_of_attempts) * 100
				if 80 <= pass_accuracy < 101: grade = 'A'
				elif 70 <= pass_accuracy < 80: grade = 'B'
				elif 60 <= pass_accuracy < 70: grade = 'C'
				elif 50 <= pass_accuracy < 60: grade = 'D'
				elif 40 <= pass_accuracy < 50: grade = 'E'
				else: grade = 'F'
				print(f'\nAttempts: {no_of_attempts}')
				print(f'Correct attempts: {correct_attempts}')
				print(f'Incorrect attempts: {incorrect_attempts}')
				print('Pass accuracy: {:.2f}% ({})'.format(pass_accuracy, grade))
			if proceedQuiz == 'Y' or proceedQuiz == 'YES':	
				states = [i for i in states_capital]
				random_state = ''.join(random.sample(states,1))
				user_capital = input(f'Enter the capital for {random_state} state: ')
				user_capital = user_capital.strip().title()
				no_of_attempts += 1
				if states_capital[random_state] == user_capital.title():
					print('Bravo!... 😉')
					correct_attempts += 1
				else:
					incorrect_attempts += 1
					print('Wrong... 😢')
					for key,value in states_capital.items():
						if key == random_state:
							print(f'The capital for {key} state is {value}')	
			proceedQuiz = input('\nContinue quiz? (yes/no): ')
			proceedQuiz = proceedQuiz.strip().upper()	
			if proceedQuiz == 'N' or proceedQuiz == 'NO' : break
			else: continue
			
main()









