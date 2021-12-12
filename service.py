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
    sql_req = '''SELECT * FROM words ORDER BY RANDOM() LIMIT 1'''
    word = con.execute(sql_req)
    print("\n")
    for row in word:
        print(row[1])
    print("\n")
    response = "again"
    while response == "again":
        response = input("How it is in swedish?\n")
        if response == row[2]:
            print("\nnoice!\n")
            return True
        if response.upper == const.end:
            return False
        else:
            print("Nope. Try again\n")
            response = "again"

def return_response(response):
    if response:
        return
    else:
        return const.end