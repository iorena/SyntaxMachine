# coding=utf8
import codecs
import xml.etree.ElementTree as XML
from array import array
from generator import Generator
from utilities import Util
from dictionary import Dictionary

verbDictionary = []
nounDictionary = []
adjectives = []
adverbs = []
newAdverbs = []
newVerbs = []
nouns = []
dictionary = Dictionary()

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

        word = child.find('s').text.encode('utf-8')
        if word[0] == '-':
            continue
        if group < 50:
            nounDictionary.append((word, group, av))
        elif group > 51 and group < 77:
            verbDictionary.append((word, group, av))
        elif group == 99:
            adverbs.append((word, group, av))

        dictionary.putWord(word, group, av, '')

def loadWordClasses():

    wordclasses = []
    classDictionary = Dictionary()

    with codecs.open('sanaluokat.txt', 'r') as lines:
        for line in lines:
            index = str.find(line, '#')
            word = line[:index].decode('utf-8')
            wordc = line[index+1:index+5].decode('utf-8')
            index = str.find(line, '#', index+5)
            keywords = line[index+1:]
            if dictionary.findWord(word):
                classDictionary.putWord(word, wordc, '', keywords)
                wordclasses.append((word, wordc))


    for entry in nounDictionary:

        if classDictionary.findWord(entry[0]):
            wordc = classDictionary.getEntry(entry[0])[0]
            if wordc == 'Subs':
                nouns.append((entry[0], entry[1], entry[2], wordc[0]))
            elif wordc == "Adje" or wordc == 'Nume':
                adjectives.append((entry[0], entry[1], entry[2], wordc[0]))
    for entry in adverbs:

        if classDictionary.findWord(entry[0]):
            wordc = classDictionary.getEntry(entry[0])[0]
            if wordc == 'Adve':
                newAdverbs.append((entry[0], entry[1], entry[2], wordc[0]))


print 'Loading dictionary...'
loadDictionary()
print 'Loading wiktionary data...'
loadWordClasses()
u = Util()

print (len(verbDictionary), ' verbs') + (len(nouns), ' nouns') + (len(adjectives), ' adjectives')


g = Generator(verbDictionary, nouns, adjectives, newAdverbs, u.auxVerbs())

while (1):
    g.generate()
    x = raw_input()

    if x == 'quit':
        break
    elif x[:6] == 'define':
        print dictionary.defineWord(x[7:])
