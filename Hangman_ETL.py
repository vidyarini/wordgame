import pymysql
from random import randint, choice

# conncet to DB
conn = pymysql.connect("127.0.0.1", user="root", passwd="password", db="Hangman", port=3306)
curr = conn.cursor()

#Easy words
File_object = open(r"C:\Users\vidya\Desktop\Easy_words.txt", "r")
File = File_object.read()
Word_array = File.split("\n")

for word in Word_array:
     query = "Insert into Easy(word) values('{}')".format(word)
     curr.execute(query)


#Hard_words
File_object = open(r"C:\Users\vidya\Desktop\Hard_words.txt", "r")
File = File_object.read()
Word_array = File.split("\n")

for word in Word_array:
     query = "Insert into Hard(word) values('{}')".format(word)
     curr.execute(query)

conn.commit()



























