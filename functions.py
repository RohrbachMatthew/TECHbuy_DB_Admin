from tabulate import tabulate
from datetime import date



#  PRODUCTS
def select_all_products(cursor):
    """
    - Selects all rows from the products table
    :return:
    all rows and columns from the products table
    """
    #  Execute SQL with cursor
    cursor.execute('Select * from products')
    #  Fetch all rows
    rows = cursor.fetchall()
    #  Headers for the table
    headers = ['ProductID', 'Serial Number', 'Product Name', 'Category', 'Price',
               'Manufacturing Cost', 'Quantity', 'Image_url']
    #  Print table
    print(tabulate(rows, headers=headers, tablefmt='grid'))

def search_products(cursor):
    """
    - prompts user for a query to filter by (column name)
    - prompts user for value to query with
    - value replaces placeholder in a query (injection prevention)
    - executes a query with the value
    - prints rows that match the user's column and value
    :return:
    searched product row and its information
    """
    user_column = input("Enter a column to filter with: ")
    user_search = input("Enter value to search by: ")
    query = f"Select * from products where {user_column} = %s"
    value = [user_search]
    cursor.execute(query, value)
    result = cursor.fetchall()

    headers = ['ProductID', 'Serial Number', 'Product Name', 'Category', 'Price',
               'Manufacturing Cost', 'Quantity', 'Image_url']

    print(tabulate(result, headers=headers, tablefmt='grid'))

def add_new_product(cursor, connection):
    """
    Adds a new product to the products table
    :param connection:
    :param cursor:
    :return:
    """
    product_name = input("Enter the name of the product: ")
    product_serial = input("Enter serial number of product: ")
    product_category = input("Enter the category: ")
    product_price = input("Enter the price of the product: ")
    product_manufacturing = input("Enter the cost of manufacturing: ")
    product_quantity = input("Enter the quantity: ")
    product_image = input("Enter the image URL: ")

    query = (f'insert into products (serial_number, product_name, category, price, manufacturing_cost, '
             f'stock_quantity, image_url) '
             f'values (%s, %s, %s, %s, %s, %s, %s)')
    value = [product_serial, product_name, product_category, product_price,
             product_manufacturing, product_quantity, product_image]
    cursor.execute(query, value)
    #  Commit the addition of a product
    connection.commit()
    print(f"Added product {product_name}, serial number {product_serial}, in category {product_category}, "
          f"price {product_price}, manufacturing price {product_manufacturing}, quantity of {product_quantity}")

def edit_products_table(cursor):
    print("Still working on this....")


#  MEMBERS
def select_all_members(cursor):
    cursor.execute('Select * from members')
    rows = cursor.fetchall()
    headers = ['MemberID', 'First Name', 'Last Name', 'Phone', 'Email', 'Date Of Birth',
               'Country', 'City', 'Address', 'Joined Date']

    print(tabulate(rows, headers=headers, tablefmt='grid'))

def search_members(cursor):
    """
    - prompts user for a query to filter by (column name)
    - prompts user for value to query with
    - value replaces placeholder in a query (injection prevention)
    - executes a query with the value
    - prints rows that match the user's column and value
    :return:
    the member row and its data
    """
    user_column = input("Enter the column to filter with: ")
    user_search = input("Enter value to search by: ")
    query = f"select * from members where {user_column} = %s"
    value = [user_search]
    cursor.execute(query, value)
    rows = cursor.fetchall()
    headers = ['MemberID', 'First Name', 'Last Name', 'Phone', 'Email', 'Date Of Birth',
               'Country', 'City', 'Address', 'Joined Date']
    print(tabulate(rows, headers=headers, tablefmt='grid'))

def add_new_member(cursor, connection):
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone = input("Enter phone number: ")
    email = input("Enter Email: ")
    d_o_b = input("Enter Date Of Birth: ")
    country = input("Enter country of residence: ")
    address = input("Enter address: ")

    get_date = date.today()
    date_today = f'{get_date:%Y-%m-%d}'

    query = (f'insert into members (firstname, lastname, phone, email, date_of_birth, member_country, '
             f'member_address, joined_date)'
             f'Values (%s, %s, %s, %s, %s, %s, %s, %s)')
    value = [first_name, last_name, phone, email, d_o_b, country, address, date_today]
    cursor.execute(query, value)
    connection.commit()


def edit_members_table(cursor):
    print("Still working on this....")


#  TRANSACTIONS
def select_all_transactions(cursor):
    print("Still working on this....")
    cursor.execute('select * from transactions')
    rows = cursor.fetchall()
    headers = ['SaleID', 'memberID', 'productID', 'products_sold', 'Total_sale', 'country',
               'date', 'year', 'month', 'day']
    print(tabulate(rows, headers=headers, tablefmt='grid'))

def search_transactions(cursor):
    print("Still working on this....")

def add_transaction(cursor):
    print("Still working on this....")

def edit_transactions(cursor):
    print("Still working on this....")

