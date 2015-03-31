# -*- coding: utf-8 -*-
import codecs
import re
import xml.etree.ElementTree as XML
from array import array

words = []

with codecs.open('../resources/recovered_data.xml', 'r', 'utf-8') as infile:
    word = ''
    wordClass = '

    for line in infile:
        line = line.encode('utf-8')
        line = str(line)
        line = str.strip(line)
        if line[:7] == '<title>':
            endIndex = str.find(line, '</')
            word = line[7:endIndex]
            continue

        text = '<text xml:space="preserve">==Suomi'
        if line[:len(text)] == text:
            line = next(infile).encode('utf-8')
            if line[:3] == '===':
                endIndex = str.find(line, '===', 1)
                wordClass = line[3:endIndex]
                description = ''
                line = next(infile).encode('utf-8')
                if line[:2] == '{{':
                    line = next(infile).encode('utf-8')
                    line = next(infile).encode('utf-8')
                    if line[0] == '#':
                        description = line[2:]
                words.append((word, wordClass, description))


words.sort()
f = codecs.open('sanaluokat.txt', 'w', 'utf-8')

for line in words:
    writeLine = line[0].decode('utf-8') + '#' + line[1].decode('utf-8') + '#' + line[2].decode('utf-8') + '\n'
    f.write(writeLine)

f.close()
