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

    def __init__(self, verbs, nouns, adjs, advbs, auxVerbs):
        self.verbs = verbs
        self.nouns = nouns
        self.adjectives = adjs
        self.adverbs = advbs
        self.auxVerbs = auxVerbs
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
        if not phrase.has_key(pos):
            phrase[pos] = np

        if rnd.randint(0, 6) > 5:
            phrase[np.partOfSpeech + 'nattr'] = self.createPossessorNoun()
        if rnd.randint(0, 6) > 4:
            phrase[np.partOfSpeech + 'aattr'] = self.createAdjective(np.partOfSpeech, np.plural)


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
        ind = rnd.randint(0, len(self.adjectives)-1)
        word = self.adjectives[ind]
        return Noun(word, pos, plural)

    def printPhrase(self, phrase):
        wordlist = []
        pos = ('subjnattr', 'subjaattr', 'subj', 'pred', 'infv', 'objnattr', 'objaattr', 'obj', 'advlnattr', 'advlaattr', 'advl')
        for x in pos:
            if phrase.has_key(x):
                wordlist.append(phrase[x].word)
        print ' '.join(wordlist)

