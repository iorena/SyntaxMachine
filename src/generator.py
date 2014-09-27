# coding=utf8
import random as rnd
from wordclasses import *


class Generator:

	conjunctions = [ 'ja',
			'kun',
			'jos',
			'vaikka' ]
		

	def __init__(self, verbs, nouns):
		self.verbs = verbs
		self.nouns = nouns
		rnd.seed()


	def generate(self):
		length = rnd.randint(1, 3)
		sentence = ''

	
		for x in range(length):
			if x > 0:
				sentence += ' ' + self.conjunctions[rnd.randint(0, len(self.conjunctions)-1)] + ' '
			ind = rnd.randint(0, len(self.nouns)-1)
			word = self.nouns[ind]
			np = Noun(word[0], word[1], word[2], 'subj', rnd.randint(0, 1)) 

			ind = rnd.randint(0, len(self.verbs)-1)
			word = self.verbs[ind]
			vp = Verb(word[0], word[1], word[2])

			ind = rnd.randint(0, len(self.nouns)-1)
			word = self.nouns[ind]
			npp = Noun(word[0], word[1], word[2], 'obj', rnd.randint(0, 1)) 

			#inflect words

			if x == 0:
				sentence += ' '.join((np.word.capitalize(), vp.word, npp.word))
			else:
				sentence += ' '.join((np.word, vp.word, npp.word))

		print sentence	
