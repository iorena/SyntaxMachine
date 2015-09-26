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


        if word.av == 'D' and self.ucode.find(word.word, 'aika') != -1: #special case: aika->ajan type change
            return self.ucode.replace(word.word, 'aika', 'aja')

        ind = self.ucode.rfind(word.word, rule[0])

        if word.type == 'verb' and word.group in [53, 58, 61]:
            return word.word
        #else if word.group in [67, 73]:

        if ind == -1:
            ind = self.ucode.rfind(word.word, rule[1])
            returnWord = self.ucode.slice(word.word, 0, ind) + rule[0] + self.ucode.slice(word.word, ind+len(rule[1]))
        else:
            returnWord = self.ucode.slice(word.word, 0, ind) + rule[1] + self.ucode.slice(word.word, ind+len(rule[0]))

        if word.av == 'D' and self.ucode.find(returnWord, 'aaa') != -1:
                return self.ucode.replace(returnWord, 'aaa', 'aa\'a')
        return returnWord
