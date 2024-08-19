#!/usr/bin/python3
""" Returns to-do list information for a given employee id."""

import requests
import sys

def todo_progress(employee_id):
    url_user = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    url_todos = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    
    # Fetch employee information
    user_response = requests.get(url_user)
    if user_response.status_code != 200:
        print(f"Error fetching user data: {user_response.status_code}")
        return
    user_data = user_response.json()
    name = user_data["name"]

    # Fetch TODO list information
    todos_response = requests.get(url_todos)
    if todos_response.status_code != 200:
        print(f"Error fetching TODO data: {todos_response.status_code}")
        return
    tasks = todos_response.json()
    total = len(tasks)

    completed_tasks = [task for task in tasks if task['completed']]
    done = len(completed_tasks)

    # Print the TODO list progress
    print(f"Employee {name} is done with tasks({done}/{total}):")
    for task in completed_tasks:
        print(f"\t {task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py EMPLOYEE_ID")
    else:
        try:
            employee_id = int(sys.argv[1])
            todo_progress(employee_id)
        except ValueError:
            print("Please enter a valid integer for the employee ID.")

