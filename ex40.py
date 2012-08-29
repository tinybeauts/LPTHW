class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics
	
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
			
	def count_lyrics(self):
		x = 0
		for line in self.lyrics:
			x += 1
		print x

happy_bday = Song(["Happy birthday to you",
				   "I don't want to get sued",
				   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
						"With pockets full of shells"])

grillz = Song(["Got thirty down at the bottom, thirty mo at the top",
			   "All invisible set in little ice cube blocks",
			   "If I could call it a drink, call it smile on da rocks",
			   "If I could call out a price, let's say, I call out a lot",
			   "I got like platinum and white gold, traditional gold",
			   "I'm changin' grillz everyday, like Jay change clothes"])

grillz_var = ["Got thirty down at the bottom, thirty mo at the top",
			  "All invisible set in little ice cube blocks",
			  "If I could call it a drink, call it smile on da rocks",
			  "If I could call out a price, let's say, I call out a lot",
			  "I got like platinum and white gold, traditional gold",
			  "I'm changin' grillz everyday, like Jay change clothes"]

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

grillz.sing_me_a_song()

Song(grillz_var).sing_me_a_song()

Song(grillz_var).count_lyrics()