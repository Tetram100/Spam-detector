import os, sys
import isspam

#Return the number of spams in a folder
def spam_detector(data):
	# We secure the opening of the directory
	try:
		os.chdir(data)

		files = os.listdir(".")

		spam_detected = 0
		mails =[]

		print "Beginning of the analysis of " + data
		#We put the mails in the RAM
		print "We put the mails in the RAM..."
		for mail in files:
			text = open(mail, "r").read()
			mails.append(text)

		#We examine each mail
		print "We analyze each mail ..."
		for mail in mails:
			if isspam.is_spam(mail) == "spam":
				spam_detected += 1

		print "The number of spams detected in the directory " + data +" is " + str(spam_detected) + " over " + str(files.__len__()) + " mails"
		return spam_detected

	except OSError:
		print "No such directory: " + data

#If we want to use directly this fonction in the terminal
if __name__ == "__main__":
	# If there isn't an argument with the script call
	if len(sys.argv) == 1:

		#We let the choice of the directory
		data = raw_input("Write the path of the directory: ")

	# Else we use the given argument
	else: 
		data = sys.argv[1] 

	#To simplify our case
	if os.path.isdir(data +"/spam") and os.path.isdir(data +"/non-spam"):
		spam_detector(data +"/spam")
		os.chdir("../../")
		spam_detector(data +"/non-spam")
	else:
		result = spam_detector(data)

	if len(sys.argv) == 3 and sys.argv[2] == "web":
		print result