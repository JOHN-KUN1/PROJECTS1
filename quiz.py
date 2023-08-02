# counter = 0

# question = input('is today monday? (yes/no): ')
# question2 = input('is today sunny? (yes/no): ')
# question3 = input('is today rainy? (yes/no): ')

# if question == 'yes':
# 	counter += 1
# if question2 == 'yes':
# 	counter += 1
# if question3 == 'no':
# 	counter +=1

# print(counter)

import random
while True:
	print('Welcome to my rock paper scissors game')
	options = ['rock', 'paper', 'scissors']
	user_input = input(f'select: {options}: ')
	computer_input = random.choice(options)
	print(computer_input)

	if user_input == 'rock'and computer_input == 'paper':
		print(f'computer played {computer_input}, you lose!')
	
	if user_input == 'scissors'and computer_input == 'rock':
		print(f'computer played {computer_input}, you lose!')
	
	if computer_input == 'paper'and user_input == 'scissors':
		print(f'computer played {computer_input}, you Win!')

	if computer_input == 'rock'and user_input == 'paper':
		print(f'computer played {computer_input}, you Win!')
	
	if computer_input == 'scissors'and user_input == 'rock':
		print(f'computer played {computer_input}, you Win!')
	
	if user_input == 'paper'and computer_input == 'scissors':
		print(f'computer played {computer_input}, you lose!')

	if user_input == computer_input:
		print(f'computer played {computer_input}!')
		print('game is a tie')
		
