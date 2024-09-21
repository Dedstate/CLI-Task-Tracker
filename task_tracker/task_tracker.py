from pathlib import Path
import json
from task_tracker.task import Task


class TaskTracker:
    def __init__(self):
        self.tasks_path = Path("tasks.json")
        self.check_file_exists()
        self.index = self.get_index()

    def check_file_exists(self):
        if not self.tasks_path.exists():
            with self.tasks_path.open("w") as f:
                json.dump([], f)

    def get_index(self):
        """Get the current index for new tasks."""
        with self.tasks_path.open("r") as json_data:
            try:
                tasks = json.load(json_data)
                return len(tasks)
            except json.JSONDecodeError:
                return 0

    def load_tasks(self):
        """Load tasks from the JSON file and convert them to Task objects."""
        with self.tasks_path.open("r") as json_data:
            try:
                tasks_dict = json.load(json_data)
                return [Task.from_dict(task) for task in tasks_dict]
            except json.JSONDecodeError:
                return []

    def save_tasks(self, tasks):
        """Save a list of Task objects to the JSON file."""
        with self.tasks_path.open("w") as json_data:
            tasks_dict = [task.to_dict() for task in tasks]
            json.dump(tasks_dict, json_data)

    def add_task(self, task_name):
        """Add a new task to the task list."""
        tasks = self.load_tasks()
        new_task = Task(self.index, task_name)
        tasks.append(new_task)
        self.index += 1
        self.save_tasks(tasks)

    def remove_task(self, task_index):
        """Remove a task by its index."""
        tasks = self.load_tasks()
        tasks = [task for task in tasks if task.task_id != task_index]

        for i, task in enumerate(tasks):
            task.task_id = i

        self.index = len(tasks)
        self.save_tasks(tasks)

    def change_status(self, task_index):
        """Change the status of a task by its index."""
        tasks = self.load_tasks()
        for task in tasks:
            if task.task_id == task_index:
                task.status = "[x]" if task.status == "[_]" else "[_]"
                break
        self.save_tasks(tasks)

    def list_tasks(self):
        """List all tasks."""
        tasks = self.load_tasks()
        for task in tasks:
            print(task)

    def list_completed_tasks(self):
        """List only completed tasks."""
        tasks = self.load_tasks()
        completed_tasks = [task for task in tasks if task.status == "[x]"]
        for task in completed_tasks:
            print(task)

    def list_uncompleted_tasks(self):
        """List only uncompleted tasks."""
        tasks = self.load_tasks()
        uncompleted_tasks = [task for task in tasks if task.status == "[_]"]
        for task in uncompleted_tasks:
            print(task)
