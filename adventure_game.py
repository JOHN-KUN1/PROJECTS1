def hauntedRoom():
	print('you\re at the final phase of the cave.')
	print('you are quite lucky to end up here in such a quick time.')
	print('all you have to do is to pick one final door.')
	directions = ['right', 'left', 'forward']
	door = input(f'which door do you follow: {directions}: ')
	if door not in directions:
		print(f'please select an option: {directions}')
	elif door == 'right':
		print('you fall into a pit and die')
		quit()
	elif door == 'left':
		print('you fall into a pit and die')
	elif door == 'forward':
		print('Congratulations!!! Adventurer , you have found an exit.')
		quit()

def showSkeletons():
	print('You see a skeletal figure in front of you.')
	print('This time around you don\'t run and approach it')
	print('fortunately it only wants for you to leave but to that it showes you three doors \"Adventurer i\'ll give you only one chance pick a door immediately!!, pick the wrong door and you die')
	directions = ['right', 'left', 'forward']
	door = input(f'Which door will you follow: {directions}: ')
	if door not in directions:
		print(f'please select an option: {directions}: ')
	elif door == 'right':
		print('you fall into a pit and die.')
		quit()
	elif door == 'left':
		hauntedRoom()
	elif door == 'forward':
		print('you fall into a pit and die.')

		quit()
def showShadow_figure():
	print('You see a dark figure at a distance. You feel terrified.')
	print('You see three openings by your right and you head for them.')
	direction = input('Which opening do you follow (right, left, forward): ')
	directions = ['right', 'left', 'forward']
	print(f'{directions}')
	if direction not in directions:
		print(f'please select an option: {directions}')
	elif direction == "right":
		hauntedRoom()
	elif direction == "left":
		print('A swarm of goblins emerge from deep within you try to fight them off but you could\'nt and you\'re killed.')
		quit()
	elif direction == "foward":
		print('You run forward and the darker it becomes. Unfortunately you fall into a pit and die!')
		quit()

def introscene():
	print('You are now in the cave and are at crossroad.')
	directions = ['forward', 'right', 'left']
	direction = input(f'which direction would you like to follow: {directions}: ').lower().strip()
	if direction not in directions:
		print(f'options: {directions}')
	elif direction == 'forward':
		showShadow_figure()
	elif direction == 'right':
		hauntedRoom()
	elif direction == 'left':
		showSkeletons()

if __name__=='__main__':
		print('Welcome to my Game.')
		print('In this game you are being chased by a monster and therefore enter a cave.')
		print('To find your way out you must choose directions to follow. And you can\'t go back' )
		print('Let\'s Begin!')
		name = input('What is your name adventurer: ')
		print(f'Goodluck {name}')
		introscene()


