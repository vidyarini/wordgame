import pymysql
from random import randint, choice

File_object = open(r"C:\Users\vidya\Desktop\Medium_words.txt", "r")

File = File_object.read()
Word_array = File.split("\n")



# conncet to DB
conn = pymysql.connect("127.0.0.1", user="root", passwd="password", db="Hangman", port=3306)
curr = conn.cursor()

for word in Word_array:
     query = "Insert into Easy(word) values('{}')".format(word)
     curr.execute(query)#
conn.commit()






















