"""
This is a program to access the database to manipulate the database
a password is needed for access
    Uses:
        - View tables
        - Filter rows by column name and value
        - Enter new data
        - Edit data
"""

import mysql.connector
from mysql.connector import Error
import functions

def main_menu_message():
    print("\nEnter selection number and press enter to continue\n"
          "1. Products Menu\n2. Members Menu\n3. Transactions menu\n4. Quit (or type quit)")

while True:
    """ DATABASE CONNECTION
    - Prompts user for a password to access the database
    - Trys to connect to the database, raises error if it occurs
    - If connection is successful a cursor is created and ends the loop
    - If error occurs user is prompted to try again
    """
    print("Welcome to the database administration program\n"
          "Use the menu and follow instructions to manipulate the database.\n")

    #  Password to be used for the database
    pass_word = input("Enter the password then press enter to continue: ")


    connection = None
    #  Try/except for connection
    try:
        connection = mysql.connector.connect(
            host='sql5.freesqldatabase.com',
            user='sql5764068',
            password=pass_word,
            database='sql5764068'
        )
        if connection.is_connected():
            print("Connection successful!")

    except Error as e:
        print(f"An error occurred: {e} ")

    #  Create cursor only when connected
    if connection is not None and connection.is_connected():
        cursor = connection.cursor()
        break
    else:
        print('Incorrect Password\nTry Again')

# Main loop start
user = ''
while user != "quit":
    main_menu_message()
    user = input("Enter selection: ").lower()
    if user == "quit":
        print("Exiting")
        break

    #  Products menu
    elif user == '1':
        while True:
            print("\nProducts Menu:\n1. View all products\n2. Search for a product\n3. "
                  "Add a new product\n4. Edit products table\n5. Exit products menu")
            sub_user = input("Type selection then press enter: ")
            #  View all products
            if sub_user == '1':
                functions.select_all_products(cursor)
                input("Press Enter to Continue")
            #  Search in products
            elif sub_user == '2':
                functions.search_products(cursor)
            # Add new product
            elif sub_user == '3':
                functions.add_new_product(cursor, connection)
            # Edit the product table
            elif sub_user == '4':
                functions.edit_products_table(cursor)
            # Exit the product menus go back to the main menu
            elif sub_user == '5':
                break
            else:
                print("invalid selection")

    #  Member menu
    elif user == '2':
        while True:
            print("Members menu:\n1. View all members\n2. Search for a member\n3. Add a member\n"
                  "4. Edit a members information\n5. Exit the members menu")
            sub_user = input("Enter selection: ")
            #  View all members
            if sub_user == '1':
                functions.select_all_members(cursor)
                input("Press enter to continue")
            #  search for a member
            elif sub_user == '2':
                functions.search_members(cursor)
            #  Add new member
            elif sub_user == '3':
                functions.add_new_member(cursor, connection)
            #  Edit the member table
            elif sub_user == '4':
                functions.edit_members_table(cursor)
            # Exit member menu
            elif sub_user == '5':
                break
            else:
                print("Invalid selection")

    # Transactions menu
    elif user == '3':
        while True:
            print("Transactions menu:\n1. View all transactions\n2. Search for a transactions\n3. Add a transactions\n"
                  "4. Edit transactions\n5. Exit the transactions menu")
            sub_user = input("Enter your selection: ")
            #  View transactions menu
            if sub_user == '1':
                functions.select_all_transactions(cursor)
                input("Press enter to continue")
            #  Search transactions
            elif sub_user == '2':
                functions.search_transactions(cursor)
            #  Add transactions
            elif sub_user == '3':
                functions.add_transaction(cursor)
            #  Edit transactions
            elif sub_user == '4':
                functions.edit_transactions(cursor)
            #  Exit transactions menu
            elif sub_user == '5':
                break
            else:
                print("Invalid selection")

    # Exit the program menu
    elif user == '4':
        print("\nExiting Program")
        break
    else:
        print("Invalid input")
#  Main loop end

#  Close out cursor and connection
cursor.close()
connection.close()
