# -*- coding: utf-8 -*-
import codecs
import re
import xml.etree.ElementTree as XML
from array import array

words = []

with codecs.open('../resources/fiwiktionary-20140920-pages-meta-current.xml', 'r') as infile:
    word = 'penis'
    wordClass = 'penis'

    for line in infile:
        line = str(line)
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
                description = ''
                line = next(infile)
                if line[:2] == '{{':
                    line = next(infile)
                    line = next(infile)
                    if line[0] == '#':
                        description = line[2:]
                words.append((word, wordClass, description))


words.sort()
f = codecs.open('sanaluokat.txt', 'w')

for line in words:
    f.write(line[0] + '#' + line[1] + line[2] + '\n')

f.close()
