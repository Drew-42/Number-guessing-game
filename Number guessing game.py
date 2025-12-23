import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0

print('XXX - Python Number Guessing Game - XXX')

while True:
	print('\n' + f'Select a number between {lowest_num} and {highest_num}')
	guess = input('Enter your guess (q to quit): ').lower()

	if guess.isdigit():
		guess = int(guess)
		guesses += 1

		if guess < lowest_num or guess > highest_num:
			print('\n' + 'Number outside of range')
		elif guess < answer:
			print('\n' + 'Too low! Try again!')
		elif guess > answer:
			print('\n' + 'Too high! Try again!')
		else:
			print('\n' + f'You got it! The answer was indeed {guess}!')
			print(f'Number of guesses: {guesses}')
			break

	elif guess == 'q':
		break

	else:
		print('Invalid guess')