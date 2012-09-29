## Trivial Pursuit
from random import random
from sys import exit
from math import *
import pink
import green
import blue
import orange
import brown
import yellow

color = ['Red', 'Green', 'Blue', 'Orange', 'Purple', 'Yellow']

## Start

class Game(object):
	
	def __init__(self):
		self.intro = [
			"Welcome to Trivial Pursuit!",
			"What color do you want to be?\n"
			]
	
	def start(self):
		for i in range(0, len(self.intro)):
			print self.intro[i]
		play = Game()
		play.pick_color()
	
	def pick_color(self):		
		for i in color:
			print color.index(i) + 1, i
		
		color_choice = raw_input("\n> ")
		pick_a_color = Check()
		pick_a_color.what_color(color_choice)

class Check(object):
	
	def __init__(self):
		pass
	
	def what_color(self, color_choice):
		if color_choice.isdigit() in range(1, len(color) + 1):
			color_choice = color[int(color_choice) - 1]
			print color_choice
		elif color_choice.title() in color:
			color_choice = color_choice.title()
			print color_choice
		elif color_choice.isalpha():
			# misspelling
			split_color_choice = []
			split_color = []
			for i in range(0, len(color_choice)):
				split_color_choice.append(color_choice[i].lower())
			for i in range(0, len(color)):
				split_color.append([])
				for x in range(0, len(color[i])):
					split_color[i].append(color[i][x].lower())
			z = []
			for i in range(0, len(split_color)):
				z.append('')
				for n in range(0, len(split_color_choice)):
					if split_color_choice[n] in split_color[i]:
						z[i] += '1'
					else:
						z[i] += '0'
			for i in range(0, len(z)):
				if (z[i] == '1'*len(z[i]) or z[i] == '1'+'0'*(len(z[i]) - 1)) and len(z[i]) == len(color[i]):
					color_choice = color[i]
			# short version
			for i in range(0, len(color)):
				if color_choice in color[i].lower():
					color_choice = color[i]
			print color_choice
			play = Check()
			play.yes_no(color_choice)
		else:
			exit(0)
	
	def yes_no(self, adjusted_input):
		print "\nDid you mean %s? y/n" % adjusted_input
		
		y_n = raw_input("> ")
		
		if y_n == 'Yes' or y_n == 'yes' or y_n == 'y'or y_n == adjusted_input.lower():
			color_choice = adjusted_input
			print color_choice
		elif y_n == 'No' or y_n == 'no' or y_n == 'n':
			print "\nOkay. Select a new color."
			y_n = Game()
			y_n.pick_color()
		else:
			print "\nSorry, I didn't catch that."
			print "Why don't you try picking a new color."
			y_n = Game()
			y_n.pick_color()			


play = Game()
play.start()