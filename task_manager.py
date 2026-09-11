import json
import os


class TaskManager:
    def __init__(self):
        self.file_name = "tasks.json"
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if not os.path.exists(self.file_name):
            return []

        with open(self.file_name, "r") as file:
            return json.load(file)

    def save_tasks(self):
        with open(self.file_name, "w") as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, employee, description, priority):
        task = {
            "id": len(self.tasks) + 1,
            "employee": employee,
            "description": description,
            "priority": priority,
            "completed": False
        }
    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return

        print("\n=== All Tasks ===")

        for task in self.tasks:
            status = "Completed" if task["completed"] else "Pending"

            print(
                f'ID: {task["id"]} | '
                f'Employee: {task["employee"]} | '
                f'Task: {task["description"]} | '
                f'Priority: {task["priority"]} | '
                f'Status: {status}'
            )

        self.tasks.append(task)
        self.save_tasks()

        print("Task added successfully.")