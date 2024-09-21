class Task:
    def __init__(self, task_id, task_name, status="[_]"):
        self.task_name = task_name
        self.task_id = task_id
        self.status = status

    def __str__(self):
        return f"ID: {self.task_id}\nTask: {self.task_name} {self.status}"

    def to_dict(self):
        """Convert the task object to a dictionary for JSON serialization."""
        return {
            "id": self.task_id,
            "task": self.task_name,
            "status": self.status,
        }

    @classmethod
    def from_dict(cls, task_dict):
        """Create a Task object from a dictionary."""
        return cls(
            task_id=task_dict["id"],
            task_name=task_dict["task"],
            status=task_dict["status"],
        )
