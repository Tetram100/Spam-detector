import string, os, sys
from db import *

#To separate each word in a text
def separate_words(text):
	#We separe each word
	words = text.lower().split(" ")
	#We remove the doubloon
	words = list(set(words))
	#We remove the "" caractere
	words = [x for x in words if x != ""]

	return words

#To remove the punctuation and the symbole
def beautiful_text(text):
	text = text.translate(string.maketrans("",""), string.punctuation)
	text = text.translate(string.maketrans("\n\t\r", "   "))

	return text

#To clear the database
def clear_db(name):
	if os.path.isfile(name):
		cursor.execute("DROP TABLE IF EXISTS words_spam")
		cursor.execute("DROP TABLE IF EXISTS words_ham")
		cursor.execute("DROP TABLE IF EXISTS stat")
