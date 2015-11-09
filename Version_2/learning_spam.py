import sys, os, sqlite3
from db import *
from helpers import *

def learning_spam (data):
	# We create the table in the database if it doesn't exist and an index to accelerate the research
	cursor.execute("CREATE TABLE IF NOT EXISTS words_spam(id INTEGER PRIMARY KEY, word VARCHAR(256), occurence INTEGER)")
	cursor.execute("CREATE INDEX IF NOT EXISTS words_spam_word_idx ON words_spam (word)")
	db.commit()

	# We secure the opening of the directory
	try:
		os.chdir(data)

		files = os.listdir(".")

		#We create the dictionary
		cursor.execute("SELECT * FROM words_spam")
		table1 = [element[1] for element in cursor.fetchall()]
		cursor.execute("SELECT * FROM words_spam")
		table2 = [element[2] for element in cursor.fetchall()]
		table_word = dict(zip(table1,table2))
		
		counter = 0
		mails = []
		
		print "We put the mails in the RAM"

		for mail in files:
			
			#We extract the text
			text = open(mail, "r").read()
			text = beautiful_text(text)

			#We put the mails in the RAM
			mails.append(text)

		#We separe the text of each mail
		for text2 in mails:

			words = separate_words(text2)

			# For each word we look if it is already in the database and we complete the dictionary
			for word in words:
				
				#Security
				word = str(word)

				#If the word is already in the database we update the entry
				if word in table_word:
					table_word[word] += 1
				#We add it otherwise
				else:
					table_word[word] = 1

			#counter += 1
			#print str(counter) + " mails analized"
		
		#We update the database
		print "We save the database"

		for new_word in table_word:
			cursor.execute("SELECT * FROM words_spam WHERE word = ?", (new_word,))
			present = cursor.fetchone()
			if present is None:
			    cursor.execute("INSERT INTO words_spam(word, occurence) VALUES(?,?)", (new_word, table_word[new_word]))
			else:
				prev_occur = present[2]
				cursor.execute("UPDATE words_spam SET occurence = ? WHERE word = ? ",(prev_occur + table_word[new_word],new_word))

		#We update the number of mails analyzed
		cursor.execute("CREATE TABLE IF NOT EXISTS stat(id INTEGER PRIMARY KEY, name VARCHAR(256), value INTEGER)")

		cursor.execute("SELECT * FROM stat WHERE name = ?", ("nbr_mails_spam",))
		present = cursor.fetchone()
		if present is None:
		    cursor.execute("INSERT INTO stat(name, value) VALUES(?,?)", ("nbr_mails_spam", len(files)))
		else:
			value = present[2]
			cursor.execute("UPDATE stat SET value = ? WHERE name = ? ",(value + len(files), "nbr_mails_spam"))

		print "analysis is finished"

	except OSError:
		print "No such directory: " + data

	db.commit()

if __name__ == "__main__":
	# If there isn't an argument with the script call
	if len(sys.argv) == 1:

		#We let the choice of the directory
		data = raw_input("Write the path of the directory: ")

	# Else we use the given argument
	else: 
		data = sys.argv[1] 

	learning_spam(data)
	db.close()