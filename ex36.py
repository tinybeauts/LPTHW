from sys import exit
import random

all_rooms = ['kitchen', 'ballroom', 'conservatory', 'billiard room', 'library', 
			'study', 'hall', 'lounge', 'dining room', 'cellar']
all_weapons = ['candlestick', 'knife', 'lead pipe', 'revolver', 'rope', 'wrench']
all_chars = ['miss scarlet', 'colonel mustard', 'mrs. white', 'reverend green',
			'mrs. peacock', 'professor plum', 'dr. black']
			
# print all_chars, all_weapons, all_rooms

poss_chars = all_chars[0:len(all_chars) - 1]
poss_rooms = all_rooms[0:len(all_rooms) - 1]

# print poss_chars, poss_rooms

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

# print good_chars, good_weapons, good_rooms

card_room = good_rooms[random.randint(0, len(good_rooms) - 1)]
card_weapon = good_weapons[random.randint(0, len(good_weapons) - 1)]
card_char = good_chars[random.randint(0, len(good_chars) - 1)]

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
		
		make_move(0)
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
		print "we know it was NOT %s in the %s with the %s." % (card_char, card_room, card_weapon)
	elif want_to_know == 5:
		print "\nyou should from room to room and see if you can solve the murder."
		print "each turn guess a murderer, weapon, and location."
		print "you can only guess the location of the room you are in."
		print "if another guest can prove you wrong, they will and your turn will be over."
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
	
def make_move(step):
	if step == 0:
		print "which room do you want to start in, %s?" % char
		first_room()

def first_room():
	if char == poss_chars[0]
		print "the lounge or the hall"
	elif char == poss_chars[1]
	
def dead(why):
	print why
	exit(0)
	
start()