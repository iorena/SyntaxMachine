# coding=utf8
import xml.etree.ElementTree as XML
from array import array
from generator import Generator


verbDictionary = []
nounDictionary = []

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
		print word




loadDictionary()
g = Generator(verbDictionary, nounDictionary)

while (1):
	g.generate()
	x = raw_input()

	if x == 'quit':
		break
