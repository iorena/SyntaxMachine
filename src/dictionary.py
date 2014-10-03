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

    def putWord(self, word, group, pv, keywords, keysentence):
        self.dictionary[self.hash(word)][self.hash(word[1:])][word] = (group, pv, keywords, keysentence)

    def getEntry(self, word):
        return self.dictionary[self.hash(word)][self.hash(word[1:])].get(word)

    def defineWord(self, word):
        definition = self.dictionary[self.hash(word)][self.hash(word[1:])].get(word)[2]
        if definition is None:
            return 'No definition'
        return ' '.join(definition)

    def getSentence(self, word):
        sentence = self.dictionary[self.hash(word)][self.hash(word[1:])].get(word)[3]
        if sentence is None:
            return 'No sentence'
        return sentence


    def varjoDefineWord(self, word):
        return self.dictionary[self.hash(word)][self.hash(word[1:])].get(word)[2]

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
