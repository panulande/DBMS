import sqlite3

# Connect to the SQLite database (it will be created if it doesn't exist)
conn = sqlite3.connect('bank.db')
cursor = conn.cursor()

# Create CUSTOMER table
cursor.execute('''
    CREATE TABLE CUSTOMER (
        customer_id INTEGER PRIMARY KEY,
        first_name TEXT,
        middle_name TEXT,
        last_name TEXT,
        dob DATE,
        mobile_number TEXT,
        gender TEXT,
        nationality TEXT,
        kyc_doc TEXT,
        pin TEXT
    )
''')

# Create BRANCH table
cursor.execute('''
    CREATE TABLE BRANCH (
        branch_id INTEGER PRIMARY KEY,
        branch_name TEXT,
        branch_location TEXT
    )
''')

# Create ACCOUNT table
cursor.execute('''
    CREATE TABLE ACCOUNT (
        account_number BIGINT PRIMARY KEY,  
        customer_id INTEGER,
        balance REAL,
        password TEXT,
        account_type TEXT,
        branch_id INTEGER,
        FOREIGN KEY (customer_id) REFERENCES CUSTOMER(customer_id),
        FOREIGN KEY (branch_id) REFERENCES BRANCH(branch_id)  -- Foreign key reference to the BRANCH table
    )
''')

# Create LOAN table
cursor.execute('''
    CREATE TABLE LOAN (
        loan_id INTEGER PRIMARY KEY,
        customer_id INTEGER,
        account_number INTEGER,
        loan_type TEXT,
        loan_amount REAL,
        interest_rate REAL,
        FOREIGN KEY (customer_id) REFERENCES CUSTOMER(customer_id),
        FOREIGN KEY (account_number) REFERENCES ACCOUNT(account_number)
    )
''')

# Create TRANSACTION table

cursor.execute('''
    CREATE TABLE "TRANSACTION" (
        transaction_id INTEGER PRIMARY KEY,
        account_number INTEGER,
        amount REAL,
        transaction_type TEXT,
        FOREIGN KEY (account_number) REFERENCES ACCOUNT(account_number)
    )
''')


# Create EMPLOYEE table
cursor.execute('''
    CREATE TABLE EMPLOYEE (
        employee_id INTEGER PRIMARY KEY,
        first_name TEXT,
        middle_name TEXT,
        last_name TEXT,
        employee_password TEXT,
        branch_id INTEGER,
        FOREIGN KEY (branch_id) REFERENCES BRANCH(branch_id)
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database 'bank.db' and tables have been created without branch_id in CUSTOMER.")

