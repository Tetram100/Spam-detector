#This script can be use to know the occurrence of a word in the mails we have, useful to know the best reccurent words

import os, sys

if len(sys.argv) == 1:
	word = raw_input("choose the word: ")
else:
	word = sys.argv[1]

nbre1 = 0
nbre2 = 0

#We begin with the non-spam email

if os.path.isdir("Dataset/non-spam"):
	data_nonspam = "Dataset/non-spam"
else:
	data_nonspam = raw_input("Write the path of the non-spam directory: ")

try:
	os.chdir(data_nonspam)
	nonspam = os.listdir(".")
except OSError:
	print "No such directory: " + data_nonspam

for mail in nonspam:
	text = open(mail, "r").read()
	occur = text.lower().count(word)
	if occur!=0:
		nbre1 = nbre1 + occur
		nbre2 += 1

print "The occurrence of " + word + " is " + str(nbre1) + " over " + str(nbre2) + " mails in the non-spam directory"

#Then we look at the spam email

if os.path.isdir("../../Dataset/non-spam"):
	data_spam = "../../Dataset/non-spam"
else:
	os.chdir("../")
	data_spam = raw_input("Write the path of the spam directory: ")

try:
	os.chdir(data_spam)
	nonspam = os.listdir(".")
except OSError:
	print "No such directory: " + data_spam

for mail in nonspam:
	text = open(mail, "r").read()
	occur = text.lower().count("word")
	if occur!=0:
		nbre1 = nbre1 + occur
		nbre2 += 1

print "The occurrence of " + word + " is " + str(nbre1) + " over " + str(nbre2) + " mails in the spam directory"
