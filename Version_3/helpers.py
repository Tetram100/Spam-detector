import string, os, sys, math, operator
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

#To clear the db without deleting it
def clear_db(name):
	if os.path.isfile(name):
		cursor.execute("DROP TABLE IF EXISTS words_spam")
		cursor.execute("DROP TABLE IF EXISTS words_ham")
		cursor.execute("DROP TABLE IF EXISTS stat")

#To make the product of each element in a table
def product(s):
	if s:
		return reduce(operator.mul, s)

#An implementation of the Inverse Chi-Square Function
def chi2P(chi, df):
    """Return prob(chisq >= chi, with df degrees of freedom).

    df must be even.
    """
    assert df & 1 == 0
    # XXX If chi is very large, exp(-m) will underflow to 0.
    m = chi / 2.0
    sum = term = math.exp(-m)
    for i in range(1, df//2):
        term *= m / i
        sum += term
    # With small chi and large df, accumulated
    # roundoff error, plus error in
    # the platform exp(), can cause this to spill
    # a few ULP above 1.0. For
    # example, chi2P(100, 300) on my box
    # has sum == 1.0 + 2.0**-52 at this
    # point.  Returning a value even a teensy
    # bit over 1.0 is no good.
    return min(sum, 1.0)