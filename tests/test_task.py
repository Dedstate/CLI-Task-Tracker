import unittest
from task_tracker.task import Task


class TestTask(unittest.TestCase):
    def test_task_creation(self):
        task = Task(1, "Test task")
        self.assertEqual(task.task_id, 1)
        self.assertEqual(task.task_name, "Test task")
        self.assertEqual(task.status, "[_]")

    def test_task_str(self):
        task = Task(1, "Test task")
        self.assertEqual(str(task), "ID: 1\nTask: Test task [_]")

    def test_task_to_dict(self):
        task = Task(1, "Test task", "[x]")
        task_dict = task.to_dict()
        self.assertEqual(
            task_dict, {"id": 1, "task": "Test task", "status": "[x]"}
        )

    def test_task_from_dict(self):
        task_dict = {"id": 1, "task": "Test task", "status": "[x]"}
        task = Task.from_dict(task_dict)
        self.assertEqual(task.task_id, 1)
        self.assertEqual(task.task_name, "Test task")
        self.assertEqual(task.status, "[x]")
