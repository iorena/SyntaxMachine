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


    def generate(self):
        length = rnd.randint(1, 2)
        phrase = { }

        for x in range(length):
            if x > 0:
                print self.conjunctions[rnd.randint(0, len(self.conjunctions)-1)] + ' '

            self.createNounPhrase('subj', phrase)
            self.createVerbPhrase(phrase)

            if phrase['pred'].transitive:
                self.createNounPhrase('obj', phrase)
            else:
                self.createNounPhrase('adv', phrase)

            if rnd.randint(0,6) > 3:
                self.createNounPhrase('adv', phrase)

            self.printPhrase(phrase)
            phrase = { }


    def createNounPhrase(self, pos, phrase):
        ind = rnd.randint(0, len(self.nouns)-1)
        word = self.nouns[ind]
        np = Noun(word, pos, rnd.randint(0, 1))
        if not phrase.has_key(pos):
            phrase[pos] = np

        if rnd.randint(0, 6) > 5:
            phrase['nattr'+np.partOfSpeech] = self.createPossessorNoun()
        if rnd.randint(0, 6) > 4:
            phrase['aattr'+np.partOfSpeech] = self.createAdjective(np.partOfSpeech, np.plural)


    def createPossessorNoun(self):
        ind = rnd.randint(0, len(self.nouns)-1)
        word = self.nouns[ind]
        return Noun(word, 'obj', 0)

    def createVerbPhrase(self, phrase):
        if rnd.randint(0, 6) > 4:   #verb phrase with auxillary verb
            word = self.auxVerbs[rnd.randint(0, len(self.auxVerbs)-1)]
            phrase['pred'] = Verb(word, 'pred', 0)
            ind = rnd.randint(0, len(self.verbs)-1)
            word = self.verbs[ind]
            phrase['infv'] = Verb(word, 'infv', 0)

        else:                   #plain old lonely predicate
            ind = rnd.randint(0, len(self.verbs)-1)
            word = self.verbs[ind]
            phrase['pred'] = Verb(word, 'pred', 0)


    def createAdjective(self, pos, plural):
        ind = rnd.randint(0, len(self.adjectives)-1)
        word = self.adjectives[ind]
        return Noun(word, pos, plural)

    def printPhrase(self, phrase):
        for x in phrase.values():
            print x.word + ' '
