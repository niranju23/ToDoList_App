
from datetime import datetime
import sqlite3
def connect_tasks_db(): 
    db_connect = sqlite3.connect("tasks.db")
    cursor = db_connect.cursor()
    return db_connect , cursor

def create_table():
    db_connect , cursor = connect_tasks_db()
    command1 = """
                    CREATE TABLE IF NOT EXISTS Tasks 
                   (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    status TEXT NOT NULL,
                    created_at TEXT NOT NULL
                   )
                   """
    cursor.execute(command1)
    db_connect.commit()

def add_task(title):
    db_connect , cursor = connect_tasks_db()
    status = 'Pending'
    created_at = datetime.now()
    command2 = """
                INSERT INTO Tasks(title,status,created_at) 
                values(?,?,?)
                   """ 
    cursor.execute(command2,(title,status,created_at))
    
    db_connect.commit()
    print("\nTask is added succesfullly")
    
    
def view_task():
    db_connect , cursor = connect_tasks_db()
    command3 = """SELECT * FROM Tasks"""
    total_tasks = cursor.execute(command3).fetchall()

    if total_tasks ==[]:
        print("No tasks have been added")
    else:
        print(total_tasks)

def update_task(id,title):
    db_connect , cursor = connect_tasks_db()
    command4 = """UPDATE tasks SET title = ? WHERE id = ?"""
    cursor.execute(command4,(id,title))
    db_connect.commit()
    