# coding=utf8
from dictionary import *
from inflector import *
from unicodeutils import UnicodeUtils

class Word:

    inflector = Inflector()
    ucode = UnicodeUtils()

    def __init__(self, word, group, av):
        self.word = word
        self.group = group
        self.av = av

        self.harmony()

    plural = False

    def harmony(self):
        chars = list(self.word)
        if 'a' in chars or 'o' in chars or 'u' in chars:
            self.A = u'a'
            self.O = u'o'
            self.U = u'u'
        else:
            self.A = u'ä'
            self.O = u'ö'
            self.U = u'y'

    def checkAv(self):
        if self.ucode.find(self.word, self.inflector.AV.avRules[self.av][0]) == -1:
            return False
        else:
            return True

class Verb(Word):

    type = 'verb'

    def __init__(self, word, pos, plural, tense):
        self.group = word[1]
        self.tense = tense
        self.lastLetter = self.ucode.lastLetter(word[0])
        self.partOfSpeech = pos
        self.plural = plural
        self.transitive = True
        self.av= word[2]
        self.word = word[0]
        if self.av != 'X':
            self.siav = self.checkAv()          #katsotaan onko perusmuodossa heikko vai vahva muoto
        self.harmony()
        self.checkReflexiveness()
        print self.group
        self.word = self.inflector.conjugate(self)


    def checkReflexiveness(self):
        word = self.word
        if self.ucode.lastLetter(word) == u'ä':
            if word[-3] == self.U:
                self.transitive = False
                print 'yay'
                return
        if word[-2:] == self.U + self.A:
            self.transitive = False
            print 'yay'
            return
        D = Dictionary()
        ind = self.ucode.find(self.word, str(self.U + 't' + self.U))  #take UtU part out of word and see if it's still a word
        unrefl = word[:ind-1] + self.A
        if ind == -1:
            ind = self.ucode.find(self.word, 't' + self.U + self.A, len(self.word)-3)     #make tUA to dA change
            unrefl = word[:len(self.word)-4] + 'd' + self.A
            if ind == -1:
                return
        self.transitive = not D.findWord(unrefl)
        if not self.transitive:
            print 'omg, a reflexive verb!'



class Noun(Word):

    type = 'noun'

    def __init__(self, word, pos, plural):
        self.word = word[0]
        self.lastLetter = self.ucode.lastLetter(self.word)
        self.group = word[1]
        self.av = word[2]
        self.partOfSpeech = pos
        if self.av != 'X':
            self.siav = self.checkAv()          #katsotaan onko perusmuodossa heikko vai vahva muoto
        self.harmony()
        if plural == 1:
            self.plural = True
        self.word = self.inflector.inflect(self)


