# coding=utf8
from astevaihtelu import AV
from unicodeutils import UnicodeUtils

class Inflector:


    def __init__(self):
        self.word = ''
        self.AV = AV()
        self.ucode = UnicodeUtils()

    def inflect(self, word):        #for nouns
        self.word = word
        if word.partOfSpeech[:4] == 'subj': #and not word.plural:
            return word.word

        stem = self.stem()

        number = ''  # self.numberMorphemes(word[len(word)-1], word.group)
        case = self.caseMorpheme()

        word.word = stem + number + case

        if word.partOfSpeech[:3] == 'obj' or word.partOfSpeech[:] == 'advl':
            return self.AV.av(word)
        return word.word

    def conjugate(self, word):      #for verbs
        if word.partOfSpeech == 'infv':
            return word.word
        self.word = word
        self.word.word = self.AV.av(word)
        stem = self.stem()
        return stem + self.tenseMorpheme(word, stem)


    def stem(self):
        group = self.word.group
        wword = self.word.word
        strlen = len(wword)


        if self.word.type == 'verb' and self.word.tense == 'past' and (group == 63 or group == 64):
            return wword[0]

        if group == 41 or group == 44 or group == 47 or group == 68 or group == 62:
            return wword[:-2]
        if group == 16:
            return wword[:-2] + u'm'
        if group == 22 or group == 32 or group == 49:
            return wword
        if group == 27:
            return wword[:-2] + u'd'
        if group == 28:
            return wword[:-2] + u'n'
        if group == 31:
            return wword[:-3] + u'hd'
        if group == 33:
            return wword[:-1] + u'm'
        if group == 34:
            return wword[:-2] + self.word.O + u'm'
        if group == 35:
            return u'lämpim'
        if group == 36 or group == 37:
            return wword[:-1] + u'mm'
        if group == 38:
            return wword[:-3] + u's'
        if group == 39:
            return wword[:-1] + u'ks'
        if group == 40:
            return wword[:-1] + u'd'
        if group == 42:
            return wword[:-1] + u'h'
        if group == 45 or group == 46:
            return wword[:-1] + u'nn'
        if group >= 53 and group < 58:
            return wword[:-2]
        if group < 50:
            if self.vowel(self.word.lastLetter):
                return wword[:-1]
            else:
                return wword
        elif group > 61 and group < 66:
            return wword[:-2]
        elif group == 66 or group == 67:
            return wword[:-2]
        elif group == 69:
            return wword[:-1] + u's'
        elif group == 70:
            return wword[:-3] + u'kse'
        elif group == 71:
            return wword[:-3] + u'ke'
        elif group == 72:
            return wword[:-2] + u'ne'
        elif group == 73:
            return wword[:-2]
        elif group == 74 or group == 75:
            return wword[:-2]
        else:
            newWord = self.ucode.slice(wword, 0, -1)
            print newWord
            vowel = self.vowel(self.word.lastLetter)
            print vowel
            if not vowel:
                return wword
            newWord = self.ucode.slice(wword, 0, -1)
            print newWord
            return newWord

    def caseMorpheme(self):
        uword = self.word.word
        word = self.word
        group = word.group
        ret = ''

        if word.partOfSpeech == 'obj':
            if group == 5 or group == 6:
                ret += u'in'
            elif group < 7:
                ret += word.lastLetter + u'n'
            elif group == 7:
                ret += u'en'
            elif group < 16:
                ret += word.lastLetter + u'n'
            elif group == 16:
                ret += word.A + u'n'
            elif group < 22:
                ret += word.lastLetter + u'n'
            elif group == 22:
                ret += u'\'n'
            elif group < 34:
                ret += u'en'
            elif group < 38:
                ret += word.A + u'n'
            elif group < 41:
                ret += u'en'
            elif group == 41 or group == 44:
                ret += word.A + word.A + u'n'
            elif group < 47:
                ret += u'en'
            elif group < 50:
                ret += u'een'
        elif self.word.partOfSpeech == 'advl':
            ret = ''
            if group == 5 or group == 6:
                ret += u'iss'
            elif group == 7:
                ret += u'ess'
            elif group == 16:
                ret += word.A + u'ss'
            elif group < 22:
                ret += word.lastLetter + u'ss'
            elif group == 22:
                ret += u'\'ss'
            elif group < 34:
                ret += u'ess'
            elif group < 38:
                ret += word.A + u'ss'
            elif group < 41:
                ret += u'ess'
            elif group == 41 or group == 44:
                ret += word.A + word.A + u'ss'
            elif group < 47:
                ret += u'ess'
            elif group < 50:
                ret += u'eess'

            return ret + word.A
        return ret


    def tenseMorpheme(self, word, stem):
        group = word.group
        A = word.A
        if word.tense == 'pres':
            if group == 52:
                return stem[-1]
            if group > 52 and group < 58:
                return A + A
            if group == 61:
                return u'i'
            if group >= 62 and group < 66:
                return ''
            if group == 68:
                return ''
            if group == 73 or group == 74 or group == 76:
                return A
            if group == 75:
                return A + A
            if group == 67 or group == 69:
                return u'ee'
            return u'e'
        elif word.tense == 'past':
            if group == 56 or group == 57:
                return u'oi'
            if group == 61 or group == 62 or group == 68:
                return ''
            if group == 63 or group == 64:
                return word.word[2] + u'i'
            if group < 73:
                return u'i'
            if group < 99:
                return u'si'



    def vowel(self, char):
        if char in [u'a', u'e', u'i', u'o', u'u', u'y', u'ä', u'ö']:
            return True
        return False
