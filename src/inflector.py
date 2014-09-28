# coding=utf8
class Inflector:


	def __init__(self):
		self.word = 'penis'		
	
	avRules = { 'X': None,
		'A': ('kk', 'k'),
		'B': ('pp', 'p'),
		'C': ('tt', 't'),
		'D': ('k', ''),
		'E': ('p', 'v'),
		'F': ('t', 'd'),
		'G': ('nk', 'ng'),
		'H': ('mp', 'mm'),
		'I': ('lt', 'll'),
		'J': ('nt', 'nn'),
		'K': ('rt', 'rr'),
		'L': ('k', 'j'),
		'M': ('k', 'v') } 
		
	def inflect(self, word): 	
		if word.partOfSpeech == 'subj':
			return word.word

		stem = self.stem(word)

		number = ''  # self.numberMorphemes(word[len(word)-1], word.group)
		case = self.caseMorpheme(self.lastLetter(word.word, 1), word.group, word.vowels)

		return stem + number + case

	def conjugate(self, word):
		stem = self.stem(word)
		
		return stem + self.tempusMorpheme(self.lastLetter(word.word, 2), word.group, word.vowels)
		
	def lastLetter(self, word, i):
		return word[len(word)-i]

	def stem(self, word):
		group = word.group
		vowels = word.vowels
		word = self.av(word.word, self.avRules[word.av])
		strlen = len(word)

				

		if group == 4 or group == 14 or group == 41 or group == 44 or group == 47:
			return word[:strlen-2]
		if group == 16:
			return word[:strlen-2] + 'm'
		if group == 22 or group == 32 or group == 49:
			return word
		if group == 27:
			return word[:strlen-2] + 'd'
		if group == 28:
			return word[:strlen-2] + 'n'
		if group == 31:
			return word[:strlen-3] + 'hd'
		if group == 33:
			return word[:strlen-1] + 'm'
		if group == 34:
			return word[:strlen-2] + 't' + vowels[1] + 'm'
		if group == 35:
			return 'lämpim'
		if group == 36 or group == 37:
			return word[:strlen-1] + 'mm'
		if group == 38:
			return word[:strlen-3] + 's'
		if group == 39:
			return word[:strlen-1] + 'ks'
		if group == 40:
			return word[:strlen-1] + 'd'
		if group == 42:
			return word[:strlen-1] + 'h'
		if group == 45 or group == 46:
			return word[:strlen-1] + 'nn'
		if group < 50: 	
			return word[:strlen-1]
		elif group > 61 and group < 66:
			return word[:strlen-2]
		elif group == 66 or group == 67:
			return word[:strlen-2] + 'e'
		elif group == 69:
			return word[:strlen-1] + 'se'
		elif group == 70:
			return word[:strlen-3] + 'kse'
		elif group == 71:
			return word[:strlen-3] + 'ke'
		elif group == 72:
			return word[:strlen-2] + 'ne'
		elif group == 73 or group == 74 or group == 75:
			return word[:strlen-2] + vowels[0]
		else:
			return word[:strlen-1] 

	def caseMorpheme(self, lastLetter, group, vowels):
		if group < 7:
			return lastLetter + 'n'
		elif group == 7:
			return 'en'
		elif group < 16:
			return lastLetter + 'n'
		elif group == 16:
			return vowels[0] + 'n'
		elif group < 22:
			return lastLetter + 'n'
		elif group == 22:
			return '\'n'
		elif group < 34:
			return 'en'
		elif group < 38:
			return vowels[0] + 'n'
		elif group < 41:
			return 'en'
		elif group == 41 or group == 44:
			return vowels[0] + vowels[0] + 'n'
		elif group < 47:
			return 'en'
		elif group < 50:
			return 'een'
			
		return ''

	def tempusMorpheme(self, lastLetter, group, vowels):
		if group == 52:
			return lastLetter
		if group > 52 and group < 58:
			return vowels[0]
		if group == 61:
			return 'i'
		if group >= 62 and group < 66:
			return ''
		if group == 68 or group == 73:
			return ''
		if group == 74 or group == 76:
			return vowels[0]
		if group == 75:
			return vowels[0]
		return 'e' 


	def av(self, word, rule):
		
		if rule is None:
			return word
		rule = str(rule)
		ind = str.find(word, rule[0])
		if ind == -1:
			ind = str.find(word, rule[1])
			return word[:ind] + rule[0] + word[ind+len(rule[1]):]
		return word[:ind] + rule[1] + word[ind+len(rule[0]):]


	def vowel(self, char):
		return char in ['a', 'e', 'i', 'o', 'u', 'y', u'ä', u'ö']
