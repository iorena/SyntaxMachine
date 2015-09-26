class UnicodeUtils:

    def find(self, haystack, needle, startInd = 0):
        haystack = list(haystack)
        needle = list(needle)
        for i in range(startInd, len(haystack)):
            if haystack[i] == needle[0]:
                index = i
                nindex = 0
                while True:
                    nindex += 1
                    index += 1
                    if nindex >= len(needle): #checked all chars in needle, found match
                        return i
                    if index >= len(haystack) or haystack[index] != needle[nindex]: #chars don't match
                        return -1

        return -1

    def rfind(self, haystack, needle, endInd = 0):
        haystack = list(haystack)
        needle = list(needle)
        if len(needle) == 0:
            return -1
        for i in range(len(haystack)-1, endInd, -1):
            if haystack[i] == needle[len(needle)-1]:
                index = i
                nindex = len(needle)-1
                while True:
                    nindex -= 1
                    index -= 1
                    if nindex < 0: #checked all chars in needle, found match
                        return index+1
                    if haystack[index] != needle[nindex]: #chars don't match
                        return -1

        return -1


    def getChar(self, word, index):
        return list(word)[index]

    def lastLetter(self, word):
        charlist = list(word)
        last = charlist[len(charlist)-1]
        return last

    def slice(self, word, startInd, endInd = None):
        newWord = ''
        word = list(word)
        if endInd is None:
            word = word[startInd:]
        else:
            word = word[startInd:endInd]
        for char in word:
            newWord += char
        if type(newWord) is unicode:
            return newWord
        return newWord.decode('utf-8')

    def replace(self, word, original, replaceWith):
        ind = self.find(word, original)
        return word[:ind] + replaceWith + word[ind+len(original):]
