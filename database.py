
from datetime import datetime
import sqlite3

def connect_tasks_db(): 
    db_connect = sqlite3.connect("tasks.db")
    cursor = db_connect.cursor()
    return db_connect , cursor


def create_users_table():
    db_connect , cursor = connect_tasks_db()
    command = """
                  CREATE TABLE IF NOT EXISTS Users(
                  user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL
                  )"""
    cursor.execute(command)
    db_connect.commit()


def create_user():

    name = input("Whats your name?")
    db_connect , cursor = connect_tasks_db()
    cursor.execute("SELECT name FROM Users where name =?",(name,))
    results = cursor.fetchone()

    if results:
        cursor.execute("SELECT user_id from Users where name=?",(name,))
        user_result = cursor.fetchone()
        return user_result[0]        

    else:
        cursor.execute("INSERT INTO Users (name) values (?)",(name,))
        db_connect.commit()
        print(f"\nWelcome {name}! Your profile has been created.")
        return cursor.lastrowid
        




def create_tasks_table():
    db_connect , cursor = connect_tasks_db()
    command1 = """
                    CREATE TABLE IF NOT EXISTS Tasks 
                   (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    title TEXT NOT NULL,
                    description TEXT,
                    priority TEXT,
                    status TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    due_date TEXT,
                    completed_on TEXT,
                    FOREIGN KEY (user_id) REFERENCES Users(user_id)
                    
                   )
                   """
    cursor.execute(command1)
    db_connect.commit()



def add_task(title,description,priority,due_date,user_id):
    db_connect , cursor = connect_tasks_db()
    status = 'Pending'
    created_at = datetime.now()
    completed_on =''   
    
    
    command2 = """
                INSERT INTO Tasks(title,description,priority,status,created_at,due_date,completed_on,user_id) 
                values(?,?,?,?,?,?,?,?)
                   """ 
    
    cursor.execute(command2,(title,description,priority,status,created_at,due_date,completed_on,user_id))    
    db_connect.commit()
    print("\nTask is added succesfullly")
    
    
def sort_task(user_id):
    db_connect,cursor = connect_tasks_db() 
    cursor.execute("SELECT * FROM Tasks WHERE user_id=? ORDER BY title ",(user_id,))
    results = cursor.fetchall()
    return results

def view_tasks(user_id):
    db_connect , cursor = connect_tasks_db()
    command3 = """SELECT * FROM Tasks WHERE user_id=?"""
    total_tasks = cursor.execute(command3,(user_id,)).fetchall()

    if total_tasks ==[]:
        print("\nNo tasks have been added")
    else:
        sorting = input("Do you want to sort by title? (y/n)")
        if sorting == 'y' :
            total_tasks_sorted = sort_task(user_id)
            print(total_tasks_sorted) 

        elif sorting == 'n':
            print(total_tasks)

       
    

def check_task_exists(task_id,user_id):
    db_connect , cursor = connect_tasks_db()    
    cursor.execute("SELECT id FROM Tasks WHERE id=? and user_id=?",(task_id,user_id))
    results = cursor.fetchone()
    if results:
        return True
    else:
        return False



def update_task_title(task_id,user_id,new_title):            
    db_connect , cursor = connect_tasks_db()                  
    update_title_command = "UPDATE Tasks SET title = ? WHERE id = ? and user_id=?"
    cursor.execute(update_title_command,(new_title,task_id,user_id))
    db_connect.commit()
    print("Task title is updated successfully")


def update_task_desc(task_id,user_id,new_description):
    db_connect , cursor = connect_tasks_db()      
    update_desc_command = "UPDATE Tasks SET description = ? WHERE id = ? and user_id=?"
    cursor.execute(update_desc_command,(new_description,task_id,user_id))
    db_connect.commit()
    print("Task description is updated successfully")


def update_both(task_id,user_id,new_title,new_description):
    db_connect , cursor = connect_tasks_db()      
    update_desc_command = "UPDATE Tasks SET title = ?,description = ? WHERE id = ? and user_id=?"
    cursor.execute(update_desc_command,(new_title,new_description,task_id,user_id))
    db_connect.commit()
    print("Task title and description are updated successfully")




def mark_task_completed(user_id,task_id):
    db_connect , cursor = connect_tasks_db()
    cursor.execute("SELECT id FROM Tasks WHERE id=? and user_id=?",(task_id,user_id))
    results = cursor.fetchone()
    if results:
        cursor.execute("SELECT status FROM Tasks WHERE id=? and user_id=?", (task_id,user_id))
        results1 = cursor.fetchone()
        if results1[0] == 'Pending':
            completed_on = datetime.now().date()            
            command5 = "UPDATE Tasks SET status = 'Completed',completed_on = ? WHERE id = ? and user_id=?"
            cursor.execute(command5,(completed_on,task_id,user_id))
            
            db_connect.commit()
            print("\nStatus is updated to 'completed'")
            
        else:
            print("\nThis task is already completed and not pending anymore")
    else:
        print("\nThe task doesn't exist")


    
def delete_task(user_id,task_id):
    db_connect , cursor = connect_tasks_db()
    cursor.execute("SELECT id FROM Tasks WHERE id=? and user_id=?",(task_id,user_id))
    results = cursor.fetchone()
    if results:
        cursor.execute("DELETE FROM Tasks WHERE id=? and user_id=?", (task_id,user_id))
        db_connect.commit()
        print("\nTask is deleted successfully")
    else:
        print("\nThe task doesn't exist")


def filter_tasks(user_id,status):
    db_connect,cursor = connect_tasks_db()    
    cursor.execute("SELECT status FROM Tasks WHERE status=? and user_id=?",(status,user_id,))
    results = cursor.fetchone()
    if results:
        command6 = "SELECT * FROM Tasks WHERE status=? and user_id=?"
        
        filter_tasks = cursor.execute(command6,(status,user_id,)).fetchall()
        print(filter_tasks)
    else:
        print(f"\nThere is no tasks with {status} status")
    


def search(user_id,keyword):
    db_connect,cursor = connect_tasks_db()    
    cursor.execute("SELECT * FROM Tasks WHERE title like ? or description like ? or status like ? or priority like ? and user_id=?",("%" +keyword + "%","%" +keyword + "%","%" +keyword + "%","%" +keyword + "%",user_id))
    results = cursor.fetchall()
    if results:
        print(results)
    else:
        print("\nThere are no such key words present")
    


def filter_overdue_tasks(user_id):
    current_date = datetime.now().date()
    db_connect,cursor = connect_tasks_db() 

    cursor.execute("SELECT * FROM Tasks WHERE due_date < ? and status ='Pending' and user_id=?",(current_date,user_id))
    results = cursor.fetchall()

    if results ==[]:
        print("\nNo overdue tasks are there")

    else:
        print(results)




    

    



    


    

    



    



    
    