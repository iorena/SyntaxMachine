import xml.etree.ElementTree as XML
from array import array

words = []
dictionary = []

def loadDictionary():
        data = XML.parse('../kotus-sanalista_v1/kotus-sanalista_v1.xml')
        root = data.getroot()

        for child in root:
                t = child.find('t')
                if t is None: #not including compound words atm
                        continue
                group = int(child.find('t').find('tn').text)

                av = 'X'
                if t.find('av') is not None:
                        av = t.find('av').text

                word = child.find('s').text
                if word[0] == '-':
                        continue
                if group < 50:
                        dictionary.append((word, group, av))
                elif group > 51 and group < 77:
                        dictionary.append((word, group, av))

def wordCompare(word1, word2):
	i = 0
	if word1 == word2:
		return 0
	for char in list(word1):
		if char == '-':
			continue
		if i >= len(word2):
			return 1
		x = ord(char) - ord(word2[i])
		if x != 0:
			return x
		i += 1		
	return -1

def dictionarySearch(dictionary, word):
	highInd = len(dictionary) - 1
	middleInd = int((len(dictionary)-1) / 2)
	lowInd = 0
	while (highInd > lowInd):
		entry = dictionary[middleInd][0]
		x = wordCompare(entry, word)
		print 'can\'t find a match ;_; ' + word 
		if x == 0:
			print 'found it!'
			return middleInd
		if x > 0:
			lowInd = middleInd+1
		if x < 0:
			highInd = middleInd-1
		middleInd = int((highInd + middleInd) / 2)
	return -1
	
#loadDictionary()

with open('../resources/fiwiktionary-20140920-pages-meta-current.xml') as infile:
	word = 'penis'
	wordClass = 'penis'

	for line in infile:
		line = str.strip(line)
		if line[:7] == '<title>':
			endIndex = str.find(line, '</')
			word = line[7:endIndex]
			continue


	  	text = '<text xml:space="preserve">==Suomi'
		if line[:len(text)] == text:
			line = next(infile)
			if line[:3] == '===':
				endIndex = str.find(line, '===', 1)
				wordClass = line[3:endIndex]
				#if dictionarySearch(dictionary, word) == -1:
				#	continue
				words.append((word, wordClass))


words.sort()
f = open('sanaluokat.txt', 'r+')

for line in words:
	f.write(line[0] + '#' + line[1] + '\n')

f.close()
