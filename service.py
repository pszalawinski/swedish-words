import sqlite3
from sqlite3.dbapi2 import connect
from typing import NewType
import constants as const
import pandas as pd

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
            print("\nnoice!")
            add_point(int(row[0]))
            return True
        if response == const.end:
            return False
        if response == const.quit:
            return False
        else:
            print("Nope. Should be: " + row[2] + ". Try again.")
            print("ID of the word in table "+ str(row[0]) + "\n")
            remove_point(int(row[0]))
            response = "again"

def replace_word():
    word_id = input("Which ID?\n")
    new_word = input("How it should be?\n")
    to_replace = "SELECT swedish_word FROM words WHERE id = " + word_id.strip() + ";" 
    replace = "UPDATE words SET swedish_word = '" + new_word.strip() + "' WHERE ID = " + str(word_id) + ";" 
    will_be_replaced = con.execute(to_replace)
    for row in will_be_replaced:
        print("Word: " + row[0] + " will be replaced with word: " + new_word.strip() +".")
    con.execute(replace)
    con.commit()

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

def import_words():
    df = pd.read_excel('words.xlsx')
    swedish = "";
    polish = "";
    for index, row in df.T.iteritems():
        
        print(row[2])
        exists = '''SELECT Count(1) FROM words WHERE polish_word = ''' + "'"+str(row[1])+"'"
        print(exists)
        swedish = str(row[2])
        polish = str(row[1])
        data_tuple = (polish, swedish, 0)
        what = con.execute(exists)
        for row in what:
            print(str(row[0]))
            if row[0] == 0:
                con.execute('''INSERT INTO words (polish_word, swedish_word, counter) VALUES (?,?,?);''', data_tuple)
                print("New word is added to library: " + polish + " - " + swedish)
                con.commit()
            if row[0] == 1:
                check = '''SELECT swedish_word FROM words WHERE polish_word = ''' + "'"+polish+"'"
                print("check " + check)
                checked_word = con.execute(check)
                for row in checked_word:
                    checking_spelling(row[0], swedish, polish, data_tuple)    

#def update_word():
               

def checking_spelling(word_to_check, swedish, polish, data_tuple):
    if(word_to_check != swedish):
                        print("checked" + word_to_check)
                        to_delete = '''DELETE FROM words WHERE polish_word = ''' + "'"+polish+"'"
                        con.execute(to_delete)
                        con.commit()
                        con.execute('''INSERT INTO words (polish_word, swedish_word, counter) VALUES (?,?,?);''', data_tuple)
                        con.commit()

    