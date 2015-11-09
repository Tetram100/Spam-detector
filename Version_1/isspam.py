import math

#This fonction takes a mail and return if it's a spam or not
def is_spam(mail):

	#We use a set of suspicious words with a "power" for each word
	key_words = {"drogue":5, "http":3, "discount":2, "sell":3, "buy":3, "proposal":5,
	"!!":6, "shipping":6, "today":3, "online":3, "available":3, "viagra":7, "xanax":7, "cialis":7,
	"free":3, "$$":7, "save":6, "offer":3, "unlimited":7, "price":2, "50%":7, "password":3,
	"medecine":7, "meds":7, "sex":7, "porn":7}

	#This is the sensibility of the detection (with a low value we detect more spams)
	threshold = 0.4
	
	#We count the "power of spamming" of the mail
	counter = 0
	for word in key_words:
		occur = mail.lower().count(word)
		if occur!=0:
			counter += key_words[word]*occur

	#We normalize the counter with the length of the mail (a long text with have a high counter easier)
	indice = counter / math.log(len(mail)+1)

	if indice > threshold:
		return "spam"
	else:
		return "non-spam"
