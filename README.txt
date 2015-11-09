This is the repository of the project of the EP 2300 course Management of Networks and Networked Systems in KTH. The goal was to make a spam detector with 3 different methods. I have also made a website to have a fancy interface for testing mails. The website runs on PHP with apache and the spam analyzis in back-end is done with Python scripts. The website is online on my server at the address https://spam.dhainaut.fr and the sources are in the "Web" folder. 


* The first version used has just a few word in a dictionnary and compares it with the message, it's fast but not very powerful. The main scripts are:
	** spamDetector.py: To use it you have to write "python spamDetector.py <folder>". It will return the number of spam in your folder.
	** occurence.py: To use it you have to write "python occurence.py <word>". It will return the occurence of this word in the spam and non-spam folders.
	** test.py: A script that tests the quality of the detection on the spam and non-spam folders and gives back the confusion matrix and the ROC curve


* The second learned from a large database of mails the occurence of each word in spam and non-spam message in order to analyze the whole message with the Naive Bayes method (you can find information on http://en.wikipedia.org/wiki/Naive_Bayes_spam_filtering). It's far more powerful than the first but a little slower. The database is the "spam_db" file on the root of the repositerie and it is use for both version 2 and version 3. It is a SQlite database, very useful for small project like this one.
The main script are:
	** spamDetector.py: To use it you have to write "python spamDetector.py <folder>". It will return the number of spam in your folder.
	** learning_spam.py: To use it you have to write "python learning_spam.py <spam_folder>". It will update the database with the information given by the mails in this spam folder.
	** learning_ham.py: To use it you have to write "python learning_ham.py <ham_folder>". It will update the database with the information given by the mails in this ham folder.
	** test.py: A script that tests the quality of the detection on the spam and non-spam folders and gives back the confusion matrix and the ROC curve. This one uses the cross validation method on this specific architecture:
		Project
		|-- Dataset
		|    |-- spam1 
		|    |-- spam2
		|	 |-- ...
		|	 |-- spam5
		|    |-- non-spam1
		|    |-- non-spam2
		|    |-- ...
		|    |-- non-spam5
		+-- Version_1
		|	|-- ...
		+-- Version_2
		|	|-- ...
		+-- Version_3
		|	|-- ...
		+-- spam_db
	To help you the Dataset is given as an archive in the main zip. 


* The third implements the fisher method (you can find information on http://www.linuxjournal.com/article/6467). It's a variant of the Bayes methode with improvements for the rare words. The only changes are on the isspam.py file, all the other scripts remain the same so you can look above to find information.


The quality of the detection is directly linked with the mails previously analized. The more mails we have, the more efficient the detection is.


-------IMPORTANT-------
If you have a problem with the given SQlite database executing the spamDetector.py of the version 2 or 3 it could be a problem on incompatibility of SQlite system version. If it is the case you have to build yourself the database by following this steps:
* Remove the "spam_db" file on the root of the repository
* Execute "python /Version_2/learning_ham.py <ham_folder>" to learn from your ham folder.
* Execute "python /Version_2/learning_spam.py <spam_folder>" to learn from your spam folder.
Now the database is completed and you can use it.