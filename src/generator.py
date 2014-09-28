# coding=utf8
import random as rnd
from wordclasses import *


class Generator:

	conjunctions = [ 'ja',
			'kun',
			 'mutta',
			'jos',
			'vaikka' ]
		

	def __init__(self, verbs, nouns, adjs):
		self.verbs = verbs
		self.nouns = nouns
		self.adjectives = adjs
		rnd.seed()


	def generate(self):
		length = rnd.randint(1, 3)
		sentence = ''

	
		for x in range(length):
			if x > 0:
				sentence += ' ' + self.conjunctions[rnd.randint(0, len(self.conjunctions)-1)] + ' '
			np = self.createNounPhrase('subj')
			
			vp = self.createVerb()

			npp = self.createNounPhrase('obj')
 
			if x == 0:
				sentence += ' '.join((np.word.capitalize(), vp.word, npp.word))
			else:
				sentence += ' '.join((np.word, vp.word, npp.word))

		print sentence	



	def createNounPhrase(self, pos):
		ind = rnd.randint(0, len(self.nouns)-1)
		word = self.nouns[ind]
		np = Noun(word, pos, rnd.randint(0, 1)) 
		if rnd.randint(0, 6) > 3:
			np = self.createAdjective(np.partOfSpeech, np.plural) + ' ' + np

		return np


	def createVerb(self):
		ind = rnd.randint(0, len(self.verbs)-1)
		word = self.verbs[ind]
		return Verb(word)

	def createAdjective(self, pos, plural):
		ind = rnd.randint(0, len(self.adjectives)-1)
		word = self.adjectives[ind]
		return Noun(word, pos, plural)
