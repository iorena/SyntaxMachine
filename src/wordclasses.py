# coding=utf8
from inflector import *

class Word:

	inflector = Inflector() 

	def __init__(self, word, group, av):
		self.word = word
		self.group = group
		self.av = av

		self.harmony()
	
	plural = False	

	def harmony(self):
		chars = list(self.word)
		if 'a' in chars or 'o' in chars or 'u' in chars:
			self.vowels = ['a', 'o', 'u']
		else:
			self.vowels = [u'ä', u'ö', 'y']

class Verb(Word):

	type = 'verb'
	
	def __init__(self, word):
		self.group = word[1] 
 		self.av= word[2] 
		self.word = word[0]
		self.harmony()
		print self.group
		self.word = self.inflector.conjugate(self)

	partOfSpeech = 'pred'
	

class Noun(Word):
	
	type = 'noun'

	def __init__(self, word, pos, plural):
		self.word = word[0]
		self.group = word[1]
		self.av = word[2]
		self.partOfSpeech = pos
		self.harmony()
		if plural == 1:
			self.plural = True
		self.word = self.inflector.inflect(self)


