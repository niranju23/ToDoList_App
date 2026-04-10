
import database

def welcome_page():
     print("""
Welcome to To-Do App
1. Add Task
2. View All Tasks
3. Update Task
4. Mark Task as Completed
5. Delete Task
6. Filter Tasks
7. Exit
""")
     
n = 0
while n!=7: 
      welcome_page()
      n = int(input("Please choose the number from the above options"))
            
      if n not in range(1,8):
          print("\nYou chose the wrong number! Please choose the right option")
      elif n==1:
        database.add_task(title=input("Enter the task name ").capitalize())
      elif n==2:
        database.view_task()
      elif(n==3):
        database.update_task(task_id=int(input("Please enter the task id to change the title")))
      elif(n==4):
        database.mark_task_completed(task_id=int(input("Please enter the task id to change the status")))
      elif(n==5):
        database.delete_task(task_id=int(input("Please enter the task id to delete the task")))
      elif(n==6):
        database.filter_tasks(status = input("Please enter the status to filter the tasks").capitalize())
      else:
          print("Goodbye!")

      
         
          