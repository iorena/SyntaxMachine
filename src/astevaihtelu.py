class AV:

    avRules = { 'X': None,
            'A': ('kk', 'k'),
            'B': ('pp', 'p'),
            'C': ('tt', 't'),
            'D': ('k', ''),
            'E': ('p', 'v'),
            'F': ('t', 'd'),
            'G': ('nk', 'ng'),
            'H': ('mp', 'mm'),
            'I': ('lt', 'll'),
            'J': ('nt', 'nn'),
            'K': ('rt', 'rr'),
            'L': ('k', 'j'),
            'M': ('k', 'v') }


    def av(self, word):		#try longer rule first, if it doesn't fit, assume
        rule = self.avRules[word.av]

        if rule is None:
            return word.word
        if word.type == 'verb' and word.siav:
            return word.word


        ind = str.rfind(word.word, rule[0])

        if ind == -1:
            ind = str.rfind(word.word, rule[1], len(word.word)/2)
            return word.word[:ind] + rule[0] + word.word[ind+len(rule[1]):]
        return word.word[:ind] + rule[1] + word.word[ind+len(rule[0]):]

#todo: add check for aika->aian type mistake
