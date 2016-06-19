import nltk

from nltk.corpus import wordnet as wn
from nltk.tree import *

word = wn.synset('.n.01')
hyp = lambda s:s.hypernyms()
tree = word.tree(hyp)

from pprint import pprint
pprint(tree)

str = str(tree)
str = str.replace("Synset", "")
str = str.replace("(", "")
str = str.replace(")", "")
str = str.replace("'", "")
str = str.replace(",", "")
str = str.replace(" ", "")
list_char = list(str)

result = ""
level = 0

index = 0

#parse tree with a stack to get only 1st and 2nd levels
while index < len(list_char):
	if list_char[index] == '[':
		level += 1
		index += 1
	elif list_char[index] == ']':
		level -= 1
		index +=1
	else:
		if level <= 2:
			while list_char[index] != '.':
				result += list_char[index]
				index += 1

			while list_char[index] != '[' and list_char[index] != ']':
				index += 1

			result += '\n'

		else:
			index +=1

#removes the last line increment
result = result[:-1]
result = result.replace("_", " ")

print(result)