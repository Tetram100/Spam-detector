import sqlite3

#We select the database we will use
db = sqlite3.connect('../spam_db')
db.text_factory = str
cursor = db.cursor()