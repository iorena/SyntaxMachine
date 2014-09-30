import codecs

class Util:


    def auxVerbs(self):
        auxVerbs = (('saada', 63, 'X', 'V'),
                    ('aikoa', 52, 'D', 'V'),
                    ('haluta', 75, 'X', 'V'),
                    ('voida', 62, 'X', 'V'))
        return auxVerbs

    def parseKeywords(self, keywords):
        keyList = []
        read = 0
        while True:
            ind = str.find(keywords, '[[', read)
            if ind == -1:
                break
            endInd = str.find(keywords, '|', ind)
            endInd2 = str.find(keywords, ']]', ind)
            if endInd != -1:
                endInd = min(endInd, endInd2)
            else:
                endInd = endInd2
            read = endInd2
            keyList.append(keywords[ind+2:endInd])
        return keyList

    def writeDown(self, wordList):
        f = open('definitions1.txt', 'w')
        for entry in wordList:
            word = entry[0].decode('utf-8')
            definition = ' '.join(entry[1]).decode('utf-8')
            if len(entry[1]) == 0:
                continue
            f.write(word + ' ' + definition + '\n')
        f.close()
