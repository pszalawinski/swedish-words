import sqlite3
from sqlite3.dbapi2 import connect


con = sqlite3.connect('words.db')
cur = con.cursor()

print("Witaj w nauce szwedzkich słówek.\n Wpisz jedną z opcji:\n")
print("START - jesli chcesz zaczac nauke.\n")
print("DODAJ - jesli chcesz dodac slowko.\n")
print("KONIEC - jesli chcesz zakonczyc nauke.\n")

def insert_new_word(polish, swedish):
    data_tuple = (polish, swedish, 0)
    con.execute('''INSERT INTO words (polish_word, swedish_word, counter) VALUES (?,?,?);''', data_tuple )
    con.commit()
    print("New word is added to library: " + polish + " - " + swedish)

polishw = "cytryna"
swedishw = "en citron"

insert_new_word(polishw, swedishw)

cursor = con.execute("SELECT * from words")
for row in cursor:
  print(row)


print ("Operation done successfully")
con.close()




