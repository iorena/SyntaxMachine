words = []

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
				words.append((word, wordClass))

words.sort()
f = open('sanaluokat.txt', 'r+')

for line in words:
	f.write(line[0] + '#' + line[1] + '\n')

f.close()
