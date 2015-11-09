from __future__ import division
import math, string
from db import *
from helpers import *

#We create the dictionaries from the database
cursor.execute("SELECT * FROM stat WHERE name = ?", ("nbr_mails_spam",))
nbr_mails_spam_analyzed  = cursor.fetchone()[2]
cursor.execute("SELECT * FROM stat WHERE name = ?", ("nbr_mails_ham",))
nbr_mails_ham_analyzed  = cursor.fetchone()[2]

#This function return the probability of a mail with this word being a spam, it is use for the next function
def proba_word(word, table_word_spam, table_word_ham, s = 1, x = 0.5):

	n1 = 0
	n2 = 0

	if word in table_word_spam:
		n1 = table_word_spam[word]

	if word in table_word_ham:
		n2 = table_word_ham[word]

	n = n1 + n2
	bw = n1 / nbr_mails_spam_analyzed
	gw = n2 / nbr_mails_ham_analyzed

	#To avoid division by 0 with exclude the case when both are 0
	if (bw !=0 or gw !=0):
		pw = bw / (bw + gw)
	else:
		pw = 0

	fw = ( (s*x) + (n*pw) ) / (s+n)
	
	return fw

#This fonction takes a mail and return if it's a spam or not
def is_spam(mail, table_word_spam, table_word_ham):

	threshold = 0.5

	#We extract the words from the mail
	text = beautiful_text(mail)
	words = separate_words(text)
	
	proba1 = []
	proba2 = []

	#We secure the computing
	try:
		for word in words:
			pw = proba_word(word, table_word_spam, table_word_ham)
			if pw != 0:
				proba1.append(pw)
				proba2.append( 1 - pw)

		#We avoid log(0) which is not defined
		if (product(proba1)!= 0):
			H = chi2P(-2*math.log(product(proba1)),2*len(proba1))
		else:
			H = 0
		if (product(proba2)!= 0):
			S = chi2P(-2*math.log(product(proba2)),2*len(proba2))
		else:
			S = 0

		I = (1 + H - S) / 2
		
		if I > threshold:
			return "spam"
		else:
			return "non-spam"
	
	except OverflowError:
		return "non-spam"
	except ZeroDivisionError:
		return "non-spam"
	except ValueError:
		return "domain log error"