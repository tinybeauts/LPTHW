from sys import exit
import random

all_rooms = ['kitchen', 'ballroom', 'conservatory', 'billiard room', 'library', 
			'study', 'hall', 'lounge', 'dining room', 'cellar']
all_weapons = ['candlestick', 'knife', 'lead pipe', 'revolver', 'rope', 'wrench']
all_chars = ['miss scarlet', 'colonel mustard', 'mrs. white', 'reverend green',
			'mrs. peacock', 'professor plum', 'dr. black']
			
poss_chars = all_chars[0:len(all_chars) - 1]
poss_rooms = all_rooms[0:len(all_rooms) - 1]

murderer = poss_chars[random.randint(0, len(poss_chars) - 1)]
murder_weapon = all_weapons[random.randint(0, len(all_weapons) - 1)]
murder_room = poss_rooms[random.randint(0, len(poss_rooms) - 1)]

# print murderer, murder_weapon, murder_room

good_chars = poss_chars[0:poss_chars.index(murderer)] + \
	poss_chars[(poss_chars.index(murderer) + 1):len(poss_chars)]
good_weapons = all_weapons[0:all_weapons.index(murder_weapon)] + \
	all_weapons[(all_weapons.index(murder_weapon) + 1):len(all_weapons)]
good_rooms = poss_rooms[0:poss_rooms.index(murder_room)] + \
	poss_rooms[(poss_rooms.index(murder_room) + 1):len(poss_rooms)]

all_cards_left = good_chars + good_weapons + good_rooms
players_cards = []

for i in range(0, len(poss_chars)):
	player = [all_cards_left.pop(random.randint(0, len(all_cards_left) - 1)), 
	all_cards_left.pop(random.randint(0, len(all_cards_left) - 1)), 
	all_cards_left.pop(random.randint(0, len(all_cards_left) - 1))]
	players_cards.append(player)

intro_speech = """
it is a dark and stormy night.
you are having dinner in a large and drafty mansion.
the dinner is hosted by your friend dr. black.
suddenly, you hear a loud and piercing scream!
you and all the guests rush to the source of the noise.
there you find the dead body of your host, dr. black!
clearly, he was murdered.
for the sake of your friend, you must bring his murderer to justice.
will you avenge dr. black, or will you slink out into the night like a coward?
choose yes for vengeance or no for cowardice:
"""

need_to_know = ['possible murderers', 'possible murder weapons',
			'possible murder locations', 'clues', 'rules']

def start():
	print intro_speech
	play = raw_input("> ")
	
	if play == "yes" or "vengeance" in play:
		pick_character()
		
		print "\n%s, you have to hurry and find the murderer." % char
		
		get_help()
		
		make_move(0, 100)
	elif play == "no" or "coward" in play:
		dead("\nin addition to being a coward, you are lazy.")
	else:
		dead("\nthat wasn't an option. vengeance is reserved for those who can read.")

def pick_character():
	print "\ngreat! thanks for your help mr... wait, which guest are you?"
	
	for i in range(0, len(poss_chars)):
		print i+1, poss_chars[i]
	
	global char
	char = raw_input("\n> ")
	
	if char.isdigit():
		char = int(char)
		
		if char in range(1, 7):
			char = poss_chars[char - 1]
			print "\ngreat! thanks for your help %s." % char
		elif char == 7:
			dead("\noops. you're supposed to be dead dr. black!")
		else:
			dead("\nthat wasn't an option. vengeance is reserved for those who can count.")
	
	elif char in all_chars and char != 'dr. black':
		print "\ngreat! thanks for your help %s." % char
	
	elif char in all_chars and char == 'dr. black':
		dead("\noops. you're supposed to be dead dr. black!")
		
	else:
		dead("\nthat wasn't an option. vengeance is reserved for those who can spell.")

def give_info(want_help):
	if want_help == 1:
		print "\nokay. what do you want to know?"
		
		for i in range(0, len(need_to_know)):
			print (i + 1), need_to_know[i]
		
		want_to_know = raw_input("\n> ")
		
		if want_to_know.isdigit():
			want_to_know = int(want_to_know)
		elif want_to_know in need_to_know:
			want_to_know = (need_to_know.index(want_to_know) + 1)
		elif "murderer" in want_to_know:
			want_to_know = 1
		elif "weapon" in want_to_know:
			want_to_know = 2
		elif "location" in want_to_know:
			want_to_know = 3
		elif "clue" in want_to_know:
			want_to_know = 4
		elif "rule" in want_to_know:
			want_to_know = 5
		else:
			dead("that wasn't an option. vengeance will not be yours today.")
		
		info_cycle(want_to_know)
	elif want_help == 0:
		print "\nokay, let's go!"
	else:
		dead("impossible. you're useless!")
	
def info_cycle(want_to_know):
	if want_to_know == 1:
		print "\nour suspects are:"
		
		for  i in range(0, len(poss_chars)):
			print poss_chars[i]
	elif want_to_know == 2:
		print "\nthe weapon has to be one of these:"
		
		for i in range(0, len(all_weapons)):
			print all_weapons[i]
	elif want_to_know == 3:
		print "\nthe murder happened in one of these rooms:"
		
		for i in range(0, len(poss_rooms)):
			print poss_rooms[i]
	elif want_to_know == 4:
		print "\nwe know a few things already."
		for i in range(0, len(poss_chars)):
			if char == poss_chars[i]:
				clues = players_cards[i]
				print "we know the %s, the %s, and the %s were NOT involved" % \
				(clues[0], clues[1], clues[2])
	elif want_to_know == 5:
		print "\nyou should move from room to room and see if you can solve the murder."
		print "each turn you guess a murderer, weapon, and location."
		print "you can only guess the location of the room you are in."
		print "if another player can prove you wrong, they will and your turn will be over."
		print "the other players will make guesses."
		print "pay attention to their guesses so you don't repeat them."
		print "when you think you've solved the mystery, move to the cellar and guess."
		print "but hurry, you have to figure it out before someone else does."
	else:
		dead("that wasn't an option. vengeance is reserved for those who can count.")
	
	get_help()
	
def get_help():
	print "\ndo you need help?"
	print "choose yes for help or no to get started: \n"
	
	want_help = raw_input("> ")
	
	if want_help == "yes" or "y" in want_help:
		give_info(1)
	elif want_help == "no" or "n" in want_help:
		give_info(0)
	else:
		dead("that wasn't an option. no vengeance for you today.")
	
def make_move(step, room_number):
	if step == 0:
		print "\nwhich room do you want to start in, %s?" % char
		first_room()
	else:
		print "\nwhich room do you want to move to now, %s?" % char
		print "you can stay in this room, move to an adjacent room, or if you think"
		print "you've solved the case, you can move to the cellar and make your guess."
		if room_number in range(0, len(all_rooms) - 1):
			print "you are in the %s." % poss_rooms[room_number]
			print "you can move to the %s or the %s." % (poss_rooms[(room_number - 1) % 8],
			poss_rooms[(room_number + 1) % 8])
			change_room = raw_input("\n> ")
			if change_room == poss_rooms[(room_number - 1) % 8]:
				room_number = (room_number - 1) % 8
				print "great! you are in the %s." % change_room
				guess(room_number)
			elif change_room == poss_rooms[(room_number + 1) % 8]:
				room_number = (room_number + 1) % 8
				print "great! you are in the %s." % change_room
				guess(room_number)
			elif change_room == "cellar":
				room_number = 9
				guess(room_number)
			elif change_room == "stay" or change_room == poss_rooms[room_number]:
				room_number = room_number
				print "great! you are staying in the %s." % poss_rooms[room_number]
				guess(room_number)
			else:
				dead("that wasn't an option. vengeance is reserved for those who can read.")
		else:
			dead("xxx")

def first_room():
	char_index = poss_chars.index(char)
	room_opts = [(char_index - 2) % 8, (char_index - 1) % 8]
	word_room_opts = [poss_rooms[(char_index - 2) % 8], poss_rooms[(char_index - 1) % 8]]
	print "\nyou can start in the %s or the %s.\n" % (word_room_opts[0], word_room_opts[1])
	
	room_choice = raw_input("> ")
	
	if word_room_opts[0] in room_choice or room_choice in word_room_opts[0]:
		assign_room(0)
	elif word_room_opts[1] in room_choice or room_choice in word_room_opts[1]:
		assign_room(1)
	else:
		dead("that's not a room. you should just go.")

def assign_room(opt):
	char_index = poss_chars.index(char)
	room_opts = [(char_index - 2) % 8, (char_index - 1) % 8]
	word_room_opts = [poss_rooms[(char_index - 2) % 8], poss_rooms[(char_index - 1) % 8]]

	if opt == 0:
		room_choice = poss_rooms[room_opts[0]]
		print "\ngreat! you are in the %s.\n" % room_choice
		room_number = poss_rooms.index(room_choice)
		guess(room_number)
	elif opt == 1:
		room_choice = poss_rooms[room_opts[1]]
		print "\ngreat! you are in the %s.\n" % room_choice
		room_number = poss_rooms.index(room_choice)
		guess(room_number)
	else:
		dead("that's not a room. you should just go.")

def guess(room_number):
	
	check_guess = [0, 0, 0]
	check_murderer(check_guess, room_number)
	
# guess a murderer
def check_murderer(check_guess, room_number):
	print "guess a murderer.\n"

	for i in range(0, len(poss_chars)):
		print i+1, poss_chars[i]

	guess_murderer = raw_input("\n> ")

	if guess_murderer.isdigit():
		guess_murderer = int(guess_murderer)
		
		if guess_murderer in range(1, 7):
			guess_murderer = poss_chars[guess_murderer - 1]
		elif guess_murderer == 7:
			dead("\noops. you're supposed to be dead dr. black!")
		else:
			dead("\nthat wasn't an option. vengeance is reserved for those who can count.")
	
	elif guess_murderer in all_chars and guess_murderer != 'dr. black':
		guess_murderer = guess_murderer
	
	elif guess_murderer in all_chars and guess_murderer == 'dr. black':
		dead("\noops. you're supposed to be dead dr. black!")
		
	else:
		dead("\nthat wasn't an option. vengeance is reserved for those who can spell.")
	
	if guess_murderer == murderer:
		check_guess[0] = 1
	else:
		check_guess[0] = 0
	
	check_weapon(check_guess, room_number, guess_murderer)

# guess a murder weapon
def check_weapon(check_guess, room_number, guess_murderer):
	print "\nguess a murder weapon.\n"

	for i in range(0, len(all_weapons)):
		print i+1, all_weapons[i]

	guess_weapon = raw_input("\n> ")

	if guess_weapon.isdigit():
		guess_weapon = int(guess_weapon)
		
		if guess_weapon in range(1, 7):
			guess_weapon = all_weapons[guess_weapon - 1]
		else:
			dead("\nthat wasn't an option. vengeance is reserved for those who can count.")
	
	elif guess_weapon in all_weapons:
		guess_weapon = guess_weapon
		
	else:
		dead("\nthat wasn't an option. vengeance is reserved for those who can spell.")
	
	if guess_weapon == murder_weapon:
		check_guess[1] = 1
	else:
		check_guess[1] = 0
	
	check_room(check_guess, room_number, guess_murderer, guess_weapon)

# guess a murder location
def check_room(check_guess, room_number, guess_murderer, guess_weapon):
	print "\nguess a murder location.\n"

	for i in range(0, len(poss_rooms)):
		print i+1, poss_rooms[i]

	guess_room = raw_input("\n> ")

	if guess_room.isdigit():
		guess_room = int(guess_room)
		
		if guess_room in range(1, 10):
			guess_room = poss_rooms[guess_room - 1]
			check_room_number = poss_rooms.index(guess_room)
		else:
			dead("\nthat wasn't an option. vengeance is reserved for those who can count.")
	elif guess_room in poss_rooms:
		guess_room = guess_room
		check_room_number = poss_rooms.index(guess_room)
	else:
		dead("\nthat wasn't an option. vengeance is reserved for those who can spell.")
	
	if room_number != 9:
		if check_room_number == room_number:
			if guess_room == murder_room:
				check_guess[2] = 1
			else:
				check_guess[2] = 0
		else:
			print "sorry, you can only guess the room you are in."
			check_room(check_guess, room_number, guess_murderer, guess_weapon)
	else:
		if guess_room == murder_room:
			check_guess[2] = 1
		else:
			check_guess[2] = 0
	
	disprove_guess(check_guess, room_number, guess_murderer, guess_weapon, guess_room)

def disprove_guess(check_guess, room_number, guess_murderer, guess_weapon, guess_room):
	if room_number != 9:
		print "\nlet's check if any of the guests can prove your guess is wrong."
		if check_guess == [1, 1, 1]:
			print "\nno one can prove you wrong."
		else:
			char_number = poss_chars.index(char)
			if guess_murderer in players_cards[char_number]:
				print "\nyou know it wasn't %s. it was in the clues!" % guess_murderer
			elif guess_weapon in players_cards[char_number]:
				print "\nyou know it wasn't the %s. it was in the clues!" % guess_weapon
			elif guess_room in players_cards[char_number]:
				print "\nyou know it wasn't in the %s. it was in the clues!" % guess_room
			else:
				for i in range(0, len(poss_chars)):
					if guess_murderer in players_cards[i]:
						print "%s can prove it wasn't %s." % (poss_chars[i], guess_murderer)
						break
					elif guess_weapon in players_cards[i]:
						print "%s can prove it wasn't the %s." % (poss_chars[i], guess_weapon)
						break
					elif guess_room in players_cards[i]:
						print "%s can prove it wasn't the %s." % (poss_chars[i], guess_room)
						break
					else:
						print "%s can't help." % poss_chars[i]
			players_guess(room_number)
	else:
		if check_guess == [1, 1, 1]:
			print "it was %s in the %s with the %s." % (murderer, murder_room, murder_weapon)
			dead("you win!")
		else:
			print "it was %s in the %s with the %s." % (murderer, murder_room, murder_weapon)
			dead("you lose!")

def players_guess(room_number):
	print "\nnow the other guests get a turn to solve the case."
	char_guess = []
	for i in range(0, len(poss_chars)):
		char_guess.append([poss_chars[random.randint(0, len(poss_chars) - 1)], 
		all_weapons[random.randint(0, len(all_weapons) - 1)], 
		poss_rooms[random.randint(0, len(poss_rooms) - 1)]])
		if char != poss_chars[i]:
			print "\n%s guesses that it was %s with the %s in the %s." % (poss_chars[i],
			char_guess[i][0], char_guess[i][1], char_guess[i][2])
			for x in range(0, len(poss_chars)):
				if char_guess[i][0] in players_cards[x]:
					print "%s can prove it wasn't %s." % (poss_chars[x], char_guess[i][0])
					break
				elif char_guess[i][1] in players_cards[x]:
					print "%s can prove it wasn't the %s." % (poss_chars[x], char_guess[i][1])
					break
				elif char_guess[i][2] in players_cards[x]:
					print "%s can prove it wasn't the %s." % (poss_chars[x], char_guess[i][2])
					break
				else:
					print "%s can't help." % poss_chars[x]
	make_move(1, room_number)

def dead(why):
	print why
	exit(0)
	
start()