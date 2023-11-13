import sqlite3

# Function to insert data into the CUSTOMER table
def insert_customer_data(customer_data):
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO CUSTOMER (customer_id, first_name, middle_name, last_name, dob, mobile_number, gender, nationality, kyc_doc, pin)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', customer_data)
    conn.commit()
    conn.close()

# Function to insert data into the ACCOUNT table
def insert_account_data(account_data):
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO ACCOUNT (account_number, customer_id, balance, password, account_type, branch_id)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', account_data)
    conn.commit()
    conn.close()

# Function to insert data into the LOAN table
def insert_loan_data(loan_data):
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO LOAN (loan_id, customer_id, account_number, loan_type, loan_amount, interest_rate)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', loan_data)
    conn.commit()
    conn.close()

# Function to insert data into the TRANSACTION table
def insert_transaction_data(transaction_data):
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO TRANSACTION (transaction_id ,account_number, amount, transaction_type)
        VALUES (?, ?, ?, ?)
    ''', transaction_data)
    conn.commit()
    conn.close()

def insert_branch_data(branch_data):
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO BRANCH (branch_id, branch_name, branch_location)
        VALUES (?, ?, ?)
    ''', branch_data)
    conn.commit()
    conn.close()


# Function to insert data into the EMPLOYEE table
def insert_employee_data(employee_data):
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO EMPLOYEE (employee_id, first_name, middle_name, last_name, employee_password, branch_id)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', employee_data)
    conn.commit()
    conn.close()

def print_table_data(table_name):
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM {table_name}')
    rows = cursor.fetchall()

    if not rows:
        print(f"No data found in the {table_name} table.")
    else:
        print(f"Data in the {table_name} table:")
        for row in rows:
            print(row)
    
    conn.close()

import sqlite3

def delete_all_data_from_table(table_name):
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    
    try:
        cursor.execute(f'DELETE FROM {table_name}')
        conn.commit()
        print(f"All data in the {table_name} table has been deleted.")
    except sqlite3.Error as e:
        print(f"Error deleting data from {table_name}: {str(e)}")

    conn.close()

# Usage example to delete all data from the CUSTOMER table

# Usage example to print all data from the CUSTOMER table

# Function to insert data into the BRANCH table


# Example usage:
# customer_data = ('John', '', 'Doe', '1990-01-15', '1234567890', 'Male', 'US', 'ID123', '1234')
# insert_customer_data(customer_data)
# Example of inserting data into the CUSTOMER table with a custom customer_id
import sqlite3

def query_row_by_primary_key(table_name, primary_key_value):
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM {table_name} WHERE customer_id = ?', (primary_key_value,))
    row = cursor.fetchone()
    
    conn.close()

    return row

print_table_data('branch')


def update_balance(account_number, new_balance):
    # Connect to the SQLite database
    conn = sqlite3.connect('bank.db')  # Replace 'your_database.db' with your SQLite database file

    # Create a cursor to execute SQL commands
    cursor = conn.cursor()

    try:
        # Update the balance for the specified account number
        update_query = "UPDATE ACCOUNT SET balance = ? WHERE account_number = ?"
        cursor.execute(update_query, (new_balance, account_number))

        # Commit the transaction
        conn.commit()
        print(f"Balance updated for account number {account_number}. New balance: {new_balance}")

    except Exception as e:
        conn.rollback()
        print(f"Error updating balance: {e}")

    finally:
        # Close the cursor and the database connection
        cursor.close()
        conn.close()

print_table_data('CUSTOMER')
print_table_data('ACCOUNT')