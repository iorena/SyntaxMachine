# coding=utf8
from astevaihtelu import AV

class Inflector:


    def __init__(self):
        self.word = ''
        self.AV = AV()

    def inflect(self, word):        #for nouns
        self.word = word
        if word.partOfSpeech[:4] == 'subj': #and not word.plural:
            return word.word

        if word.partOfSpeech[:3] == 'obj' or word.partOfSpeech[:4] == 'advl':
            word.word = self.AV.av(word)

        stem = self.stem()

        number = ''  # self.numberMorphemes(word[len(word)-1], word.group)
        case = self.caseMorpheme()

        return stem + number + case

    def conjugate(self, word):      #for verbs
        if word.partOfSpeech == 'infv':
            return word.word
        self.word = word
        self.word.word = self.AV.av(word)
        stem = self.stem()
        return stem + self.tempusMorpheme(self.lastLetter(word.word, 2), word.group, word.A)


    def lastLetter(self, word, i):
        return word[-i]

    def stem(self):
        group = self.word.group
        wword = self.word.word
        strlen = len(wword)


        if group == 14 or group == 41 or group == 44 or group == 47 or group == 68 or group == 62:
            return wword[:strlen-2]
        if group == 16:
            return wword[:strlen-2] + 'm'
        if group == 22 or group == 32 or group == 49:
            return wword
        if group == 27:
            return wword[:strlen-2] + 'd'
        if group == 28:
            return wword[:strlen-2] + 'n'
        if group == 31:
            return wword[:strlen-3] + 'hd'
        if group == 33:
            return wword[:strlen-1] + 'm'
        if group == 34:
            return wword[:strlen-2] + self.word.O + 'm'
        if group == 35:
            return 'lämpim'
        if group == 36 or group == 37:
            return wword[:strlen-1] + 'mm'
        if group == 38:
            return wword[:strlen-3] + 's'
        if group == 39:
            return wword[:strlen-1] + 'ks'
        if group == 40:
            return wword[:strlen-1] + 'd'
        if group == 42:
            return wword[:strlen-1] + 'h'
        if group == 45 or group == 46:
            return wword[:strlen-1] + 'nn'
        if group < 50:
            return wword[:strlen-1]
        elif group > 61 and group < 66:
            return wword[:strlen-2]
        elif group == 66 or group == 67:
            return wword[:strlen-2]
        elif group == 69:
            return wword[:strlen-1] + 'se'
        elif group == 70:
            return wword[:strlen-3] + 'kse'
        elif group == 71:
            return wword[:strlen-3] + 'ke'
        elif group == 72:
            return wword[:strlen-2] + 'ne'
        elif group == 73:
            return wword[:strlen-2] + self.word.A
        elif group == 74 or group == 75:
            return wword[:strlen-2] + self.word.A
        else:
            print wword[-1]
            if not self.vowel(wword[-1]):
                return wword
            return wword[:strlen-1]

    def caseMorpheme(self):
        word = self.word
        group = word.group
        lastLetter = self.lastLetter(word.word, 1)

        if word.partOfSpeech == 'obj':
            if group == 5 or group == 6:
                return 'in'
            elif group < 7:
                return lastLetter + 'n'
            elif group == 7:
                return 'en'
            elif group < 16:
                return lastLetter + 'n'
            elif group == 16:
                return word.A + 'n'
            elif group < 22:
                return lastLetter + 'n'
            elif group == 22:
                return '\'n'
            elif group < 34:
                return 'en'
            elif group < 38:
                return word.A + 'n'
            elif group < 41:
                return 'en'
            elif group == 41 or group == 44:
                return word.A + word.A + 'n'
            elif group < 47:
                return 'en'
            elif group < 50:
                return 'een'
        elif word.partOfSpeech == 'advl':
            ret = ''
            if group == 5 or group == 6:
                ret += 'iss'
            elif group == 7:
                ret += 'ess'
            elif group == 16:
                ret += word.A + 'ss'
            elif group < 22:
                ret += lastLetter + 'ss'
            elif group == 22:
                ret += '\'ss'
            elif group < 34:
                ret += 'ess'
            elif group < 38:
                ret += word.A + 'ss'
            elif group < 41:
                ret += 'ess'
            elif group == 41 or group == 44:
                ret += word.A + word.A + 'ss'
            elif group < 47:
                ret += 'ess'
            elif group < 50:
                ret += 'eess'

            return ret + word.A
        return ''

    def tempusMorpheme(self, lastLetter, group, A):
        if group == 52:
            return lastLetter
        if group > 52 and group < 58:
            return A
        if group == 61:
            return 'i'
        if group >= 62 and group < 66:
            return ''
        if group == 68 or group == 73:
            return ''
        if group == 74 or group == 76:
            return A
        if group == 75:
            return A
        if group == 67:
            return 'ee'
        return 'e'

    def vowel(self, char):
        return char in ['a', 'e', 'i', 'o', 'u', 'y', u'ä'.encode('utf-8'), u'ö'.encode('utf-8')]

