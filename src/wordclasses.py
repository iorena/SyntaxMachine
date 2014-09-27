# coding=utf8
from inflector import *

class Word:

	inflector = Inflector() 

	def __init__(self, word, group, av):
		self.word = word
		self.group = group
		self.av = av

	
	plural = False	

	

class Verb(Word):

	type = 'verb'
	
	partOfSpeech = 'pred'
	

class Noun(Word):
	
	type = 'noun'

	def __init__(self, word, group, av, pos, plural):
		self.word = word
		self.group = group
		self.av = av
		self.partOfSpeech = pos
		if plural == 1:
			self.plural = True
		self.word = self.inflector.inflect(self)

