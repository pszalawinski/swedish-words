import sqlite3
from sqlite3.dbapi2 import connect
import constants as const

con = sqlite3.connect('words.db')
cur = con.cursor()

def insert_new_word():

    polish_word = input("Enter polish word: ")
    swedish_word = input("Enter swedish word: ")

    #jezeli slowko tutaj gdzies quit to ma wyjsc
    #dodac petle ze slowko nie moze byc empty

    data_tuple = (polish_word, swedish_word, 0)
    con.execute('''INSERT INTO words (polish_word, swedish_word, counter) VALUES (?,?,?);''', data_tuple )
    con.commit()
    print("New word is added to library: " + polish_word + " - " + swedish_word)

def menu(): 
    print("START - if you want to start learning.")
    print("ADD - if you want to add word.")
    print("END - if you want to get back to menu.")
    print("QUIT - if you want to quit from app.")

def words_menu():
    print("SHOW - show all words")

def print_all_words():
     cursor = con.execute("SELECT * from words")
     count = con.execute("SELECT COUNT(*) from words")
     for row in count:
        print("\n\nPrinting all [" + str(row[0]) +"] words:\n")
     for row in cursor:
        print(row)
     print("\n")

def practice():
    sql_req = '''SELECT * FROM words WHERE counter < 15 ORDER BY RANDOM() LIMIT 1'''
    word = con.execute(sql_req)
    print("\n")
    for row in word:
        print(row[1])
    print("\n")
    response = "again"
    while response == "again":
        response = input("How it is in swedish?\n")
        if response.strip() == row[2]:
            print("\nnoice!\n")
            print(int(row[0]))
            add_point(int(row[0]))
            return True
        if response == const.end:
            return False
        if response == const.quit:
            return False
        else:
            print("Nope. Try again\n")
            remove_point(int(row[0]))
            response = "again"

def return_response(response):
    if response:
        return
    else:
        return const.end

def add_point(id):
  sql_req = '''SELECT * FROM words where id = ''' + str(id)
  counter = con.execute(sql_req)
  for row in counter:  
    new_counter = int(row[3]) + 1
    sql_update = '''UPDATE words SET counter = ''' + str(new_counter) + ''' WHERE id = ''' + str(id)
    con.execute(sql_update)
    con.commit()

def remove_point(id):
    sql_req = '''SELECT * FROM words where id = ''' + str(id)
    counter = con.execute(sql_req)
    for row in counter:  
        new_counter = int(row[3]) - 1
        sql_update = '''UPDATE words SET counter = ''' + str(new_counter) + ''' WHERE id = ''' + str(id)
        con.execute(sql_update)
        con.commit()

def create_table():
    con.execute('''CREATE TABLE words
         (ID INTEGER PRIMARY KEY AUTOINCREMENT,
         polish_word TEXT NOT NULL,
         swedish_word TEXT NOT NULL,
         counter INT);''')
    con.commit()
    
def drop_table():
    con.execute('''DROP TABLE words;''')
    con.commit()