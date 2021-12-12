import sqlite3
from sqlite3.dbapi2 import connect
import service 
import constants as const


con = sqlite3.connect('words.db')
cur = con.cursor()


print("Hello in swedish word recap.\n Choose one of options:\n")
service.menu()

user_input = input(const.what_do)
user_input.strip()

while user_input == "":
    user_input = input(const.what_do)

while user_input.upper != "QUIT":
    if user_input.upper() == "ADD":
        service.insert_new_word()
        user_input = input(const.add_or_end)
    if user_input.upper() == "QUIT":
        print("Vi ses!")
        con.close()
        quit()
    if user_input.upper() == "START":
       while service.practice():
           user_input = const.start
       user_input = const.end
    if user_input.upper() == "SHOW":
       service.print_all_words()
       user_input = const.end
    if user_input.upper() == const.end:
        user_input = input("You are back in menu: " + const.what_do)
        while user_input == "":
            print(const.choose_sth)
            service.menu()
            user_input = input(const.what_do)
    else: 
        print("Command not recognized")
        quit()

con.close()




