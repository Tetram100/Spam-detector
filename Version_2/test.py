#You need the matploatlib module, install it with "sudo apt-get install python-matplotlib" on an ubuntu/debian machine
from __future__ import division
import os, sys, spamDetector, learning_ham, learning_spam
import matplotlib.pyplot as plt
from db import *
from helpers import *

#This function present the results from spamDetector
def presentation_results (data_spam, data_ham):
	#We analyze the spam folder
	if os.path.isdir(data_spam):
		folder_spam = data_spam
	else:
		folder_spam = raw_input("Write the path of the spam directory: ")

	TPC = spamDetector.spam_detector(data_spam)
	FNC = len(os.listdir(".")) - TPC
	TPR = TPC / (TPC + FNC)

	#We come back to the main folder and we analyze the non-spam folder
	os.chdir("../")
	if os.path.isdir(data_ham):
		folder_spam = data_ham
	else:
		folder_spam = raw_input("Write the path of the non-spam directory: ")

	FPC = spamDetector.spam_detector(data_ham)
	TNC = len(os.listdir(".")) - FPC
	FPR = FPC / (FPC + TNC)

	#We give the ascii art table
	print "---------------------------------------------------------"
	print "|                     | Actual Spam  | Actual Non-Spam  |"
	print "---------------------------------------------------------"
	print "| Classified Spam     |" + str(TPC) + "          |" + str(FPC) +"                |"
	print "---------------------------------------------------------"
	print "| Classified Non-Spam |" + str(FNC) + "            |" + str(TNC) +"              |"
	print "---------------------------------------------------------"

	os.chdir("../")
	print "The TPR is " + str(TPR)
	print "The FPR is " +str(FPR)

	return [TPR,FPR]

def analyze_folder (number1, number2 = 5):
	#We learn from the number part of the spam and non-spam
	learning_spam.learning_spam("spam" + str(number1))
	os.chdir("../")
	learning_ham.learning_ham("non-spam" + str(number1))
	os.chdir("../")

	#We analyze another part of spam and non-spam
	TPR.append(presentation_results ("spam" + str(number2), "non-spam" + str(number2))[0])
	FPR.append(presentation_results ("spam" + str(number2), "non-spam" + str(number2))[1])

if __name__ == "__main__":

	print "You have enough time to take a coffee"

	FPR = []
	TPR = []

	os.chdir("../Dataset/")

	for j in range (1,6):
		#We clean the database
		clear_db("../spam_db")
		for i in range(1,6):
			if i != j:
				analyze_folder(i,j)

	print "The analyzis is completed."

	FPR_medium = sum(FPR) / len (FPR)
	TPR_medium = sum(TPR) / len (TPR)

	print "The average TPR is " + str(TPR_medium)
	print "The average FPR is " + str(FPR_medium)

	#We plot the ROC curve with matplotlib
	fig = plt.figure()
	x = FPR
	y = TPR
	plt.plot(x, y, 'ro')
	plt.plot([0, 1], [0, 1], marker='o', linestyle='--', color='g', label='Random guess')
	plt.title('ROC Space')
	plt.plot(x, y)
	plt.xlabel('FPR')
	plt.ylabel('TPR')
	plt.legend()
	plt.show()

	print FPR
	print TPR