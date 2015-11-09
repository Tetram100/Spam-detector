from __future__ import division
import math, string
from db import *
from helpers import *


#This fonction takes a mail and return if it's a spam or not
def is_spam(mail, table_word_spam, table_word_ham):

	proportion_spam = 0.8
	threshold = 0.5

	#We extract the words from the mail
	text = beautiful_text(mail)
	words = separate_words(text)

	#We create the dictionaries from the database
	cursor.execute("SELECT * FROM stat WHERE name = ?", ("nbr_mails_spam",))
	nbr_mails_spam_analyzed  = cursor.fetchone()[2]
	cursor.execute("SELECT * FROM stat WHERE name = ?", ("nbr_mails_ham",))
	nbr_mails_ham_analyzed  = cursor.fetchone()[2]

	p1 = 1
	p2 = 1
	n1 = 0
	n2 = 0

	for word in words:
		
		#If the word is present we count it
		if word in table_word_spam:
		   	p1 = p1 * table_word_spam[word]
		   	n1 += 1

		if word in table_word_ham:
		   	p2 = p2 * table_word_ham[word]
		   	n2 += 1


	#We secure the calcul python errors
	try:
		
		#We use this algorithm to calcul proba_spam in order to avoid big number (overflow error) 
		#or too small number (rounding to 0)
		temp = 1
		i = 1
		beg = min(n1,n2)
		while i <= beg:
			temp = temp * ( nbr_mails_ham_analyzed / nbr_mails_spam_analyzed)
			i += 1
		if beg == n1:
			while i <= n2:
				temp = temp * nbr_mails_ham_analyzed
				i += 1
		if beg == n2:	
			while i <= n1:
				temp = temp / nbr_mails_spam_analyzed
				i += 1

		proba_spam = 1 / (1 + (p2 / p1) * temp * ( (1-proportion_spam) / proportion_spam) )

		if proba_spam > threshold:
			return "spam"
		else:
			return "non-spam"
	
	except OverflowError:
		return "non-spam"
	except ZeroDivisionError:
		return "non-spam"