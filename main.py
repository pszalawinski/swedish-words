import sqlite3
from sqlite3.dbapi2 import connect
import service 


con = sqlite3.connect('words.db')
cur = con.cursor()

print("Hello in swedish word recap.\n Choose one of options:\n")
service.menu()

user_input = input("What do you want to do?\n")
user_input.strip()

while user_input == "":
    user_input = input("You need to choose something. What do you want to do?\n")

while user_input.upper != "QUIT":
    if user_input.upper() == "ADD":
        service.insert_new_word()
        user_input = input("Do you want to add another [ADD] ? Or get back to menu [END]? ")
    if user_input.upper() == "QUIT":
        print("Vi ses!")
        con.close()
        quit()
    if user_input.upper() == "START":
        print("Not yet")
    if user_input.upper() == "SHOW":
       service.print_all_words()
       user_input = "END"
    if user_input.upper() == "END":
        user_input = input("You are back in menu: What do you want to do?\n")
        while user_input == "":
            print("You need to choose something.")
            service.menu()
            user_input = input("What do you want to do?\n")
    else: 
        print("Command not recognized")
        user_input = "END"



# cursor = con.execute("SELECT * from words")
# for row in cursor:
#   print(row)



con.close()




