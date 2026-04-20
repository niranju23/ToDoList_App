To-Do List App
A simple multi-user to-do list app that runs in the terminal, built with Python and SQLite3

Please run the below line in terminal to run the application
python3 main.py

Enter your name when prompted. New users are registered automatically. Existing users are recognised by name.

Features :
Add tasks with title, description, due date, and priority
View all tasks (with option to sort by title)
Update task by title, description, or both
Mark tasks as completed (completion time is recorded automatically)
Delete tasks
Filter tasks by status (Pending / Completed)
Search tasks by keyword
View overdue tasks

Menu
1. Add Task
2. View All Tasks
3. Update Task
4. Mark Task as Completed
5. Delete Task
6. Filter Tasks
7. Search by keyword
8. Filter overdue tasks
9. Exit

Requirements:
Python 3.x
SQLite3 (included with Python)

Project Structure:
├── main.py
├── database.py
├── utils.py
└── tasks.db
