
import database
import utils

def welcome_page():
     print("""

1. Add Task
2. View All Tasks
3. Update Task
4. Mark Task as Completed
5. Delete Task
6. Filter Tasks
7. Search by keyword
8. Filter overdue tasks
9. Exit
""")
     

database.create_users_table()
user_id = database.create_user()
database.create_tasks_table()
  
n = 0
while n!=9:
      welcome_page()

      try:
          n = int(input("Please choose the number from the above options"))
          
      except:
          print("\nPlease check your input!")
          continue

      if n not in range(1,10):
          print("\nYou chose the wrong number! Please choose the right option")

      elif n==1:
        title=input("Enter the task name ").capitalize()
        description=input("Enter the task description ").capitalize()
        while True:
          due_date=input("Enter the due date DD/MM/YYYY ")
          if utils.validate_date(due_date):
            break
          else:
            print("Invalid date format. Please use YYYY-MM-DD")
        database.add_task(title,description,due_date,user_id)
           
        
        
      elif n==2:
        database.view_tasks(user_id)

      elif(n==3):
        task_id = int(input("Please enter the task id: "))
        if database.check_task_exists(task_id,user_id):
           
           while True: 
              update_options = input("\nDo you wanna update title or description or both?")
              if update_options in ['title', 'description', 'both']:

                if update_options == 'title' :    
                    database.update_task_title(task_id ,user_id,new_title=input("\nEnter the new title: ").capitalize(),)
                elif update_options =='description' :
                    database.update_task_desc(task_id,user_id,new_description=input("\nEnter the new description: "))
                elif update_options == 'both' :
                    database.update_both(task_id,user_id,new_title=input("\nEnter the new title: ").capitalize(),new_description=input("\nEnter the new description: "))
                else:
                  print("\nInvalid option. Please choose title, description, or both.")
                break
              
        else:
          print("\nNo tasks exist")
          

      elif(n==4):
        database.mark_task_completed(user_id,task_id=int(input("Please enter the task id to change the status")))
      elif(n==5):
        database.delete_task(user_id,task_id=int(input("Please enter the task id to delete the task")))
      elif(n==6):
        database.filter_tasks(user_id,status = input("Please enter the status to filter the tasks").capitalize())
      elif(n==7):
         database.search(user_id,keyword=input("Please enter the keyword"))
      elif(n==8):
         database.filter_overdue_tasks(user_id,)
      else:
          print("Goodbye!")

         
         

      
         
          