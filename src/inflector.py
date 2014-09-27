# coding=utf8
class Inflector:


	def __init__(self):
		self.penis = 'penis'		
	
		

		
	def inflect(self, word): 	
		if word.partOfSpeech == 'subj':
			return word.word

		stem = self.stem(word.word)

		number = ''  # self.numberMorphemes(word[len(word)-1], word.group)
		case = self.caseMorpheme(word.word[len(word.word)-1], word.group)

		return stem + number + case

		
	def stem(self, word):
		strlen = len(word)
		if self.vowel(word[strlen-1]):
			return self.stem(word[:strlen-1])
		else:
			return word

	def caseMorpheme(self, lastLetter, group):
		if group < 7:
			return lastLetter + 'n'
		elif group == 7:
			return 'en'
		elif group < 16:
			return lastLetter + 'n'
		elif group == 16:
			return 'an'
		elif group < 22:
			return lastLetter + 'n'
		elif group == 22:
			return '\'n'
		elif group < 34:
			return 'en'
		elif group < 38:
			return 'an'
		elif group < 41:
			return 'en'
		elif group == 41 or group == 44:
			return 'aan'
		elif group < 47:
			return 'en'
		elif group < 50:
			return 'een'
			
		return ''

	def vowel(self, char):
		return char in ['a', 'e', 'i', 'o', 'u', 'y', u'ä', u'ö']
