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

        self.tasks.append(task)
        self.save_tasks()

        print("Task added successfully.")