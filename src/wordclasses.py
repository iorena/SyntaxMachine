# coding=utf8
from dictionary import *
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
            self.A = 'a'
            self.O = 'o'
            self.U = 'u'
        else:
            self.A = 'ä'
            self.O = 'ö'
            self.U = 'y'

    def checkAv(self):
        if str.find(self.word, self.inflector.AV.avRules[self.av][0]) == -1:
            return False
        else:
            return True

class Verb(Word):

    def __init__(self, word, pos, plural):
        self.group = word[1]
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
        D = Dictionary()
        ind = str.find(self.word, str(self.U + 't' + self.U))  #take UtU part out of word and see if it's still a word
        unrefl = self.word[:ind-1] + self.A
        if ind == -1:
            ind = str.find(self.word, str('t' + self.U + self.A), len(self.word)-3)     #make tUA to dA change
            unrefl = self.word[:len(self.word)-4] + 'd' + self.A
            if ind == -1:
                return
        self.transitive = not D.findWord(unrefl)
        if not self.transitive:
            print 'omg, a reflexive verb!'



class Noun(Word):

    type = 'noun'

    def __init__(self, word, pos, plural):
        self.word = word[0]
        self.group = word[1]
        self.av = word[2]
        self.partOfSpeech = pos
        if self.av != 'X':
            self.siav = self.checkAv()          #katsotaan onko perusmuodossa heikko vai vahva muoto
        self.harmony()
        if plural == 1:
            self.plural = True
        self.word = self.inflector.inflect(self)


