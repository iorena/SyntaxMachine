class Dictionary:

	dictionary = (

			( {}, {},  {},  {},  {},  {},  {},  {},  {} ),
			( {}, {},  {},  {},  {},  {},  {},  {},  {} ),
			( {}, {},  {},  {},  {},  {},  {},  {},  {} ),
			( {}, {},  {},  {},  {},  {},  {},  {},  {} ),
			( {}, {},  {},  {},  {},  {},  {},  {},  {} ),
			( {}, {},  {},  {},  {},  {},  {},  {},  {} ),
			( {}, {},  {},  {},  {},  {},  {},  {},  {} ),
			( {}, {},  {},  {},  {},  {},  {},  {},  {} ),
			( {}, {},  {},  {},  {},  {},  {},  {},  {} ),

			 )
			


	

	def findWord(self, word):
		return word in self.dictionary[self.hash(word)][self.hash(word[1:])]


	def putWord(self, word, group, pv):
		self.dictionary[self.hash(word)][self.hash(word[1:])][word] = (group, pv)


	def getEntry(self, word):
		return self.dictionary[self.hash(word)][self.hash(word[1:])].get(word)



	def hash(self, word):
		if len(word) > 0:
			c = ord(word[0])
		else:
			c = ord('z')
		if c < ord('h'):
			return 0
		if c < ord('k'):
			return 1
		if c < ord('l'):
			return 2
		if c < ord('m'):
			return 3
		if c < ord('o'):
			return 4
		if c < ord('r'):
			return 5
		if c < ord('t'):
			return 6
		if c < ord('u'):
			return 7
		return 8
