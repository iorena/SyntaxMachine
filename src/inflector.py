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
        if word.partOfSpeech[:4] == 'subj' and word.case != 'part': #and not word.plural:
            return word.word

        stem = self.stem()

        number = ''  # self.numberMorphemes(word[len(word)-1], word.group)
        if word.case == 'nom':
            case = self.caseMorpheme()
        elif word.case == 'part':
            case = self.partitiveCaseMorpheme()

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

        if group == 41 or group == 44:
            return wword[:-2] + self.word.A + self.word.A
        if group == 47:
            return wword[:-2] + u'ee'
        if group == 7 or group in range(23, 33):
            return wword[:-1] + u'e'
        if group == 48:
            return wword[:-1] + u'ee'
        if group == 16:
            return wword[:-2] + u'm' + self.word.A
        if group == 22:
            return wword + u'\''
        if group == 27:
            return wword[:-2] + u'de'
        if group == 28:
            return wword[:-2] + u'ne'
        if group == 31:
            return wword[:-3] + u'hde'
        if group == 32:
            return wword + u'e'
        if group == 33:
            return wword[:-1] + u'me'
        if group == 34:
            return wword[:-2] + self.word.O + u'm' + self.word.A
        if group == 35:
            return u'lämpimä'
        if group == 36 or group == 37:
            return wword[:-1] + u'mm' + self.word.A
        if group == 38:
            return wword[:-3] + u'se'
        if group == 39:
            return wword[:-1] + u'kse'
        if group == 40:
            return wword[:-1] + u'de'
        if group == 42:
            return wword[:-1] + u'he'
        if group == 45 or group == 46:
            return wword[:-1] + u'nne'
        if group >= 53 and group < 58:
            return wword[:-2]
        if group < 50:
            if self.vowel(self.word.lastLetter):
                return wword
            else:
                return wword + u'i'
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
            return wword[:-2] + u'n'
        elif group == 73:
            return wword[:-2]
        elif group == 74 or group == 75:
            return wword[:-2]
        else:
            newWord = self.ucode.slice(wword, 0, -1)
            vowel = self.vowel(self.word.lastLetter)
            if not vowel:
                return wword
            newWord = self.ucode.slice(wword, 0, -1)
            return newWord

    def caseMorpheme(self):
        uword = self.word.word
        word = self.word
        group = word.group
        ret = ''

        if word.partOfSpeech == 'obj':
            if group < 22:
                ret += u'n'
            elif group == 22:
                ret += u'\'n'
            elif group < 50:
                ret += u'n'
        elif self.word.partOfSpeech == 'advl':
            return u'ss' + word.A
        return ret

    def partitiveCaseMorpheme(self):
        uword = self.word.word
        word = self.word
        group = word.group
        ret = ''

        if group in [3, 17, 18, 19, 23, 24]:
            ret += u't' + word.A
        elif group == 22:
            ret += u'\'t' + word.A
        elif group < 26:
            ret += word.A
        elif group < 43:
            ret += u't' + word.A
        elif group < 47 or group == 48:
            ret += u'tt' + word.A
        elif group < 48:
            ret += u'utt' + word.A
        elif group == 49:
            ret += u't' + word.A

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
