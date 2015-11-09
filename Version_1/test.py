#You need the matploatlib module, install it with "sudo apt-get install python-matplotlib" on an ubuntu/debian machine
from __future__ import division
import os, sys, spamDetector
import matplotlib.pyplot as plt

#We analyze the spam folder
if os.path.isdir("Dataset/spam"):
	folder_spam = "Dataset/spam"
else:
	folder_spam = raw_input("Write the path of the spam directory: ")

TPC = spamDetector.spam_detector("Dataset/spam")
FNC = len(os.listdir(".")) - TPC
TPR = TPC / (TPC + FNC)

#We come back to the main folder and we analyze the non-spam folder
os.chdir("../../")
if os.path.isdir("Dataset/non-spam"):
	folder_spam = "Dataset/non-spam"
else:
	folder_spam = raw_input("Write the path of the non-spam directory: ")

FPC = spamDetector.spam_detector("Dataset/non-spam")
TNC = len(os.listdir(".")) - FPC
FPR = FPC / (FPC + TNC)

#We give the ascii art table
print "---------------------------------------------------------"
print "|                     | Actual Spam  | Actual Non-Spam  |"
print "---------------------------------------------------------"
print "| Classified Spam     |" + str(TPC) + "          |" + str(FPC) +"              |"
print "---------------------------------------------------------"
print "| Classified Non-Spam |" + str(FNC) + "          |" + str(TNC) +"              |"
print "---------------------------------------------------------"

print "The TPR is " + str(TPR)
print "The FRP is " +str(FPR)

#We plot the ROC curve with matplotlib
fig = plt.figure()
x = [FPR]
y = [TPR]
plt.plot(x, y, 'ro')
plt.plot([0, 1], [0, 1], marker='o', linestyle='--', color='g', label='Random guess')
plt.title('ROC Space')
plt.plot(x, y)
plt.xlabel('FPR')
plt.ylabel('TPR')
plt.legend()
plt.show()