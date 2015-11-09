import os, sys, sqlite3, isspam
from db import *
from helpers import *

def spam_detector(data):
	# We secure the opening of the directory
	os.chdir(data)

	files = os.listdir(".")

	#We create the dictionary of spam words
	cursor.execute("SELECT * FROM words_spam")
	table1 = [element[1] for element in cursor.fetchall()]
	cursor.execute("SELECT * FROM words_spam")
	table2 = [element[2] for element in cursor.fetchall()]
	table_word_spam = dict(zip(table1,table2))

	#We create the dictionary of ham words
	cursor.execute("SELECT * FROM words_ham")
	table1 = [element[1] for element in cursor.fetchall()]
	cursor.execute("SELECT * FROM words_ham")
	table2 = [element[2] for element in cursor.fetchall()]
	table_word_ham = dict(zip(table1,table2))

	spam_detected = 0
	#counter = 0
	mails = []

	print "Beginning of the analysis of " + data
	#We put the mails in the RAM
	print "We put the mails in the RAM..."
	for mail in files:
		text = open(mail, "r").read()
		mails.append(text)

	#We analyze each mails
	print "We analyze each mail..."
	for mail in mails:
		if isspam.is_spam(mail, table_word_spam, table_word_ham) == "spam":
			spam_detected += 1
		#counter += 1
		#print counter

	print "The number of spams detected in this directory is " + str(spam_detected) + " over " + str(files.__len__()) + " mails"

	return spam_detected


if __name__ == "__main__":
	# If there isn't an argument with the script call
	if len(sys.argv) == 1:

		#We let the choice of the directory
		data = raw_input("Write the path of the directory: ")

	# Else we use the given argument
	else: 
		data = sys.argv[1] 
	
	result = spam_detector(data)

	if len(sys.argv) == 3 and sys.argv[2] == "web":
		print result

