'''
Lee Strickland
Module 5 SQL
The purpose of Project 5 is to demostrate proficiency in SQL by creating a Pyton script that interacts with an SQL database.
'''

#Imports
import sqlite3
import pandas as pd
import pathlib

# Define database file in the root project folder
db_file = pathlib.Path("project.db")

# Define function insert records from CSV
def insert_data_from_csv():
    """Function to use pandas to read data from CSV files (in 'data' folder)
    and insert the records into their respective tables."""
    try:
        author_data_path = pathlib.Path("data", "authors.csv")
        book_data_path = pathlib.Path("data", "books.csv")
        authors_df = pd.read_csv(author_data_path)
        books_df = pd.read_csv(book_data_path)
        with sqlite3.connect(db_file) as conn:
            # use the pandas DataFrame to_sql() method to insert data
            # pass in the table name and the connection
            authors_df.to_sql("authors", conn, if_exists="replace", index=False)
            books_df.to_sql("books", conn, if_exists="replace", index=False)
            print("Data inserted successfully.")
    except (sqlite3.Error, pd.errors.EmptyDataError, FileNotFoundError) as e:
        print("Error inserting data:", e)

# Define function inserting new records to data tables
def execute_insert_records(db_file, insert_records_sql_file):
    with sqlite3.connect(db_file) as conn:
        insert_records_sql_file = pathlib.Path("insert_records.sql")
        with open(insert_records_sql_file, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {insert_records_sql_file}")

