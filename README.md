# datafun-05-sql-
Repo for Project 05 focusing on database interactions using SQLite.
Introduction:
Project 05 for class 44608 focusing on integrating Python and SQL and database interactions using SQLite.
Install and Run the Project:
Create github repository and clone to local machine.
```git clone project.url```

```python3 -m venv .venv```
```source .venv/bin/activate```
```python3 -m pip intall -r requirements.txt```

Freeze Requirements:
```python3 -m pip freeze > requirements.txt```

Import Dependencies and Create Database
```import sqline3```
```import pandad as pd```
```import pathlib```

# Define database file in current root project directory
```db_file = pathlib.Path("project.sqlite3")```

```def create_database():```
    '''Function to create database. Will create new database file if it doesn't exist. Close connection after creation of databese so as not to lock the file'''
    ```try:
           conn = sqlite3.connect(db_file)
           conn.close()
           print("Database created successfully.")
        exept sqlite3.Error as e:
            print("Error creating datavase:", e)```

```def main():
       create_database()```

```if__name__ == "__main__":
      main()```

Git Add/Commit/Push
```git add .```
```git comit -m "initial commit"```
```git puch prigin main```

Specificatons:
This project will follow specifications: https://github.com/denisecase/datafun-05-spec