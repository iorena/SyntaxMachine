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

    def __init__(self, verbs, nouns, adjs, advbs, auxVerbs, numerals):
        self.verbs = verbs
        self.nouns = nouns
        self.adjectives = adjs
        self.adverbs = advbs
        self.auxVerbs = auxVerbs
        self.numerals = numerals
        rnd.seed()

    flags = {'kari' : 0}

    def generate(self):
        length = rnd.randint(1, 2)
        phrase = { }

        for x in range(length):
            if x > 0:
                print self.conjunctions[rnd.randint(0, len(self.conjunctions)-1)] + ' '

            self.createNounPhrase('subj', phrase)
            self.createVerbPhrase(phrase)

            if phrase.has_key('infv'):
                if phrase['infv'].transitive:
                    self.createNounPhrase('obj', phrase)
                else:
                    self.createNounPhrase('advl', phrase)
            elif phrase['pred'].transitive:
                self.createNounPhrase('obj', phrase)
            else:
                self.createNounPhrase('advl', phrase)

            if rnd.randint(0,6) > 3:
                self.createNounPhrase('advl', phrase)

            self.printPhrase(phrase)
            phrase = { }


    def createNounPhrase(self, pos, phrase):
        ind = rnd.randint(0, len(self.nouns)-1)
        word = self.nouns[ind]
        np = Noun(word, pos, rnd.randint(0, 1))

        if rnd.randint(0, 6) > 5:
            phrase[np.partOfSpeech + 'nattr'] = self.createPossessorNoun()
        if rnd.randint(0, 6) > 4:
            adjective = self.createAdjective(np.partOfSpeech, np.plural)
            if np.partOfSpeech == 'subj' and adjective[1] == 'num' and adjective[0].lastLetter != 's' and adjective[0] != 'yksi': #numerals, exept 'one' and those ending in 's' which are assumed to be ordinals
                np = Noun(word, pos, 0, 'part')
            phrase[np.partOfSpeech + 'aattr'] = adjective[0]

        if not phrase.has_key(pos):
            phrase[pos] = np

    def createPossessorNoun(self):
        ind = rnd.randint(0, len(self.nouns)-1)
        word = self.nouns[ind]
        return Noun(word, 'obj', 0)

    def createVerbPhrase(self, phrase):
        if rnd.randint(0, 1) >= 0:      #random tempus
            tense = 'past'
        else:
            tense = 'pres'

        if rnd.randint(0, 6) > 4:   #verb phrase with auxillary verb
            word = self.auxVerbs[rnd.randint(0, len(self.auxVerbs)-1)]
            phrase['pred'] = Verb(word, 'pred', 0, tense)
            ind = rnd.randint(0, len(self.verbs)-1)
            word = self.verbs[ind]
            phrase['infv'] = Verb(word, 'infv', 0, tense)

        else:                   #plain old lonely predicate
            ind = rnd.randint(0, len(self.verbs)-1)
            word = self.verbs[ind]
            phrase['pred'] = Verb(word, 'pred', 0, tense)


    def createAdjective(self, pos, plural):
        r = rnd.randint(1, 6)
        if r < 6:
            ind = rnd.randint(0, len(self.adjectives)-1)
            word = self.adjectives[ind]
            return (Noun(word, pos, plural), 'adj')
        else:
            ind = rnd.randint(0, len(self.numerals)-1)
            word = self.numerals[ind]
            return (Noun(word, pos, plural), 'num')


    def printPhrase(self, phrase):
        wordlist = []
        pos = ('subjnattr', 'subjaattr', 'subj', 'pred', 'infv', 'objnattr', 'objaattr', 'obj', 'advlnattr', 'advlaattr', 'advl')
        for x in pos:
            if phrase.has_key(x):
                wordlist.append(phrase[x].word)
        print ' '.join(wordlist)

