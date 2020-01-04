#This program is for handling a client list
from typing import Any
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config


class client:
    def __init__(self, name, address, phone, email):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email

def menu():
    print("\n\nWelcome to Real Estate Client Manager V1.0")
    print("Please pay attention, as our menu options have changed.\n")
    print("-------Menu Options-------")
    print("Add     Delete     Modify\n")
    print("Enter 'Menu' at any time to return to the main menu")
    print("Enter 'Exit' at any time to quite the program\n")


#def delete():

#def modify():

client_list = []
current_client = []

current_command = " "
menu()

while True:
    current_command = input("Enter command:  ").lower()

    if current_command == 'add':
        answer = "n"
        while answer != "y":
            name = input("Name: ")
            address = input("Address: ")
            phone = input("Phone Number: ")
            email = input("Email: ")
            print("Is this information correct?")
            print(name + "\n" + address + "\n" + phone + "\n" + email + "\n")
            answer = input("y/n").lower()
        new_client = client(name, address, phone, email)
        client_list.append(new_client)

    elif current_command == 'delete':
        delete()
    elif current_command == 'modify':
        modify()
    elif current_command == 'menu':
        menu()
    elif current_command == "exit":
        print("\nThanks! Come again!")
        break




