from unicodeutils import UnicodeUtils

class AV:

    ucode = UnicodeUtils()

    avRules = { 'X': None,
            'A': (u'kk', u'k'),
            'B': (u'pp', u'p'),
            'C': (u'tt', u't'),
            'D': (u'k', u''),
            'E': (u'p', u'v'),
            'F': (u't', u'd'),
            'G': (u'nk', u'ng'),
            'H': (u'mp', u'mm'),
            'I': (u'lt', u'll'),
            'J': (u'nt', u'nn'),
            'K': (u'rt', u'rr'),
            'L': (u'k', u'j'),
            'M': (u'k', u'v') }


    def av(self, word):		#try longer rule first, if it doesn't fit, assume
        rule = self.avRules[word.av]

        if rule is None:
            return word.word
        if word.type == 'verb' and word.siav:
            return word.word


        ind = self.ucode.rfind(word.word, rule[0])

        if ind == -1:
            ind = self.ucode.rfind(word.word, rule[1])
            return word.word[:ind] + rule[0] + word.word[ind+len(rule[1]):]
        return word.word[:ind] + rule[1] + word.word[ind+len(rule[0]):]

#todo: add check for aika->aian type mistake
