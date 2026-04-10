
from datetime import datetime
import sqlite3
def connect_tasks_db(): 
    db_connect = sqlite3.connect("tasks.db")
    cursor = db_connect.cursor()
    return db_connect , cursor

table_name ='Tasks'


def create_table():
    db_connect , cursor = connect_tasks_db()
    command1 = f"""
                    CREATE TABLE IF NOT EXISTS {table_name} 
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
    command2 = f"""
                INSERT INTO {table_name}(title,status,created_at) 
                values(?,?,?)
                   """ 
    
    cursor.execute(command2,(title,status,created_at))    
    db_connect.commit()
    print("\nTask is added succesfullly")
    
    
def view_tasks():
    db_connect , cursor = connect_tasks_db()
    command3 = f"""SELECT * FROM {table_name}"""
    total_tasks = cursor.execute(command3).fetchall()

    if total_tasks ==[]:
        print("\nNo tasks have been added")

    else:
        print(total_tasks)

def update_task(new_title,task_id):
    db_connect , cursor = connect_tasks_db()
    
    cursor.execute(f"SELECT id FROM {table_name} WHERE id=?",(task_id,))
    results = cursor.fetchone()
    if results:
        
        command4 = f"UPDATE {table_name} SET title = ? WHERE id = ?"
        cursor.execute(command4,(new_title,task_id))
        db_connect.commit()
        print("\nTask is updated succesfullly")
    else:
        print("\nThe task doesn't exist")
        
    


def mark_task_completed(task_id):
    db_connect , cursor = connect_tasks_db()
    cursor.execute(f"SELECT id FROM {table_name} WHERE id=?",(task_id,))
    results = cursor.fetchone()
    if results:
        cursor.execute(f"SELECT status FROM {table_name} WHERE id=?", (task_id,))
        results1 = cursor.fetchone()
        if results1[0] == 'Pending':
            command5 = f"UPDATE {table_name} SET status = 'Completed' WHERE id = ?"
            cursor.execute(command5,(task_id,))
            db_connect.commit()
            print("\nStatus is updated to 'completed'")
        else:
            print("\nThis task is already completed and not pending anymore")
    else:
        print("\nThe task doesn't exist")

    
def delete_task(task_id):
    db_connect , cursor = connect_tasks_db()
    cursor.execute(f"SELECT id FROM {table_name} WHERE id=?",(task_id,))
    results = cursor.fetchone()
    if results:
        cursor.execute(f"DELETE FROM {table_name} WHERE id=?", (task_id,))
        db_connect.commit()
        print("\nTask is deleted successfully")
    else:
        print("\nThe task doesn't exist")


def filter_tasks(status):
    db_connect , cursor = connect_tasks_db()    
    cursor.execute(f"SELECT status FROM {table_name} WHERE status=?",(status,))
    results = cursor.fetchone()
    if results:
        command6 = f"SELECT * FROM {table_name} WHERE status=?"
        
        filter_tasks = cursor.execute(command6,(status,)).fetchall()
        print(filter_tasks)
    else:
        print(f"\nThere is no tasks with {status} status")
    
    



    



    
    