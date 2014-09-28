# coding=utf8
import random as rnd
from wordclasses import *


class Generator:

	conjunctions = [ 'ja',
			'kun',
			'että',
             'mutta',
			'jos',
			'vaikka' ]

	def __init__(self, verbs, nouns, adjs, advbs):
		self.verbs = verbs
		self.nouns = nouns
		self.adjectives = adjs
		self.adverbs = advbs
		rnd.seed()


	def generate(self):
		length = rnd.randint(1, 3)
		sentence = ''


		for x in range(length):
			if x > 0:
				sentence += self.conjunctions[rnd.randint(0, len(self.conjunctions)-1)] + ' '
			np = self.createNounPhrase('subj')

			vp = self.createVerb()

			if vp.transitive:
				npp = self.createNounPhrase('obj')
			else:
				npp = self.createNounPhrase('adv')
			advp = ''

			if rnd.randint(0,6) > 3:
				advp = self.createNounPhrase('adv')

			if x == 0:
				sentence += ' '.join((np.capitalize(), vp.word, npp, advp)) + ' '
			else:
				sentence += ' '.join((np, vp.word, npp, advp)) + ' '

		print sentence.encode('utf-8')



	def createNounPhrase(self, pos):
		ind = rnd.randint(0, len(self.nouns)-1)
		word = self.nouns[ind]
		np = Noun(word, pos, rnd.randint(0, 1))
		word = np.word
		if rnd.randint(0, 6) > 5:
			word = self.createPossessorNoun().word + ' ' + word
		if rnd.randint(0, 6) > 4:
			word = self.createAdjective(np.partOfSpeech, np.plural).word + ' ' + word


		return word


	def createPossessorNoun(self):
		ind = rnd.randint(0, len(self.nouns)-1)
		word = self.nouns[ind]
		return Noun(word, 'obj', 0)

	def createVerb(self):
		ind = rnd.randint(0, len(self.verbs)-1)
		word = self.verbs[ind]
		return Verb(word)

	def createAdjective(self, pos, plural):
		ind = rnd.randint(0, len(self.adjectives)-1)
		word = self.adjectives[ind]
		return Noun(word, pos, plural)

