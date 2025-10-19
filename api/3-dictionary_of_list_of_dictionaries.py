#!/usr/bin/python3
"""
Exports all employees' TODO list data to JSON format.
"""

import json
import requests


if __name__ == "__main__":
    # API base URL
    base_url = "https://jsonplaceholder.typicode.com"

    # Get all users
    users = requests.get(f"{base_url}/users").json()

    # Dictionary to store all user tasks
    all_tasks = {}

    for user in users:
        user_id = user.get("id")
        username = user.get("username")

        # Get this user's todos
        todos = requests.get(f"{base_url}/todos", params={"userId": user_id}).json()

        # Build task list for this user
        all_tasks[user_id] = [
            {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            for task in todos
        ]

    # Export to JSON file
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_tasks, json_file)
