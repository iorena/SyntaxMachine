# -*- coding: utf-8 -*-
import codecs
import re
import xml.etree.ElementTree as XML
from array import array

words = []


with codecs.open('../resources/recovered_data.xml', 'r', 'utf-8') as infile:
    word = ''
    wordClass = ''
    nouns = 0

    for line in infile:
        line = line.encode('utf-8')
        line = str(line)
        line = str.strip(line)
        if line[:7] == '<title>':
            endIndex = str.find(line, '</')
            word = line[7:endIndex]
            continue

        text = '==Suomi'
        altText = '<text xml:space="preserve">==Suomi'
        if line[:len(text)] == text or line[:len(altText)] == altText:
            line = next(infile).encode('utf-8')
            if line[:3] == '===':
                endIndex = str.find(line, '===', 1)
                wordClass = line[3:endIndex]
                description = ''
                firstChar = ''
                while firstChar != '=':
                    line = next(infile).encode('utf-8')
                    firstChar = line[0]
                    if firstChar == '#':
                        description += line[1:]

                words.append((word, wordClass, description))
                if wordClass[2] == 'b':
                    nouns += 1

    print nouns


words.sort()
f = codecs.open('sanaluokat.txt', 'w', 'utf-8')

for line in words:
    if type(line[2]) == unicode:
        line[2] = line[2].encode('utf-8')
    writeLine = line[0].decode('utf-8') + '#' + line[1].decode('utf-8') + '#' + line[2].decode('utf-8') + '\n'
    f.write(writeLine)

f.close()
