# coding=utf8
import xml.etree.ElementTree as XML
from array import array
from generator import Generator


verbDictionary = []
nounDictionary = []
adjectives = []
newVerbs = []
nouns = []


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

		if group < 50:
			nounDictionary.append((word, group, av))
		elif group > 51 and group < 77:
			verbDictionary.append((word, group, av))


def wordCompare(word1, word2):
	i = 0
	if word1 == word2:
		return 0
	for char in list(word1):
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
		entry = dictionary[middleInd][0].encode('utf-8')
		x = wordCompare(entry, word)
		if x == 0:
			print 'found it!'
			return middleInd
		if x > 0:
			lowInd = middleInd+1
		if x < 0:
			highInd = middleInd-1
		middleInd = int((highInd + middleInd) / 2)
	return -1
	
def loadWordClasses():


	with open('sanaluokat.txt') as lines:
		for line in lines:
			index = str.find(line, '#')
			word = line[:index]
			wordc = line[index+1:index+5]


			if wordc == "Verb":
				index = dictionarySearch(verbDictionary, word)
				if index == -1:
					continue
				entry = verbDictionary[index]
				newVerbs.append((entry[0], entry[1], entry[2], wordc[0]))
		
			elif wordc == "Subs":
				index = dictionarySearch(nounDictionary, word)
				if index == -1:
					continue
				entry = nounDictionary[index]
				nouns.append((entry[0], entry[1], entry[2], wordc[0]))

			elif wordc == "Adje":
				index = dictionarySearch(nounDictionary, word)
				if index == -1:
					continue
				entry = nounDictionary[index]
				adjectives.append((entry[0], entry[1], entry[2], wordc[0]))
		



print 'Loading dictionary...'
loadDictionary()
print 'Loading wiktionary data...'
loadWordClasses()

g = Generator(newVerbs, nouns, adjectives)

while (1):
	g.generate()
	x = raw_input()

	if x == 'quit':
		break
