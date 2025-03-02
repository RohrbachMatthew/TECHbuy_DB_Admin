# Data back up file

"""
This is a file that should run on its own to back up the entire database
- Future additions: Each time the data is updated or changed, the "main" file will
    overwrite the csv to save the data. (For main file)
- File is not scheduled and will only back up when running
"""


import mysql.connector
from mysql.connector import Error
import pandas as pd


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

cursor = connection.cursor()

#  Overwrite the csv to save the complete and updated data
def database_to_csv():
    """
    Saves data to CSV from the database

    """

    # fetches the list of tables
    try:
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()

        for table in tables:
            table_name = table[0]
            query = f'select * from {table_name}'
            cursor.execute(query)
            rows = cursor.fetchall()
            columns = [i[0] for i in cursor.description]

            df = pd.DataFrame(rows, columns=columns)
            df.to_csv(f'{table_name}_back_up.csv', index=False)
    except Exception as e1:
        print(f"Error occur {e1}.")
    finally:
        cursor.close()
        connection.close()

user = input("Would you like to save the data to csv?: ").lower()
if user == 'y':
    database_to_csv()
    print(f'saved data to csv files')
