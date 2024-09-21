import argparse
from task_tracker.task_tracker import TaskTracker


class ArgParser:
    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser(description="CLI Task Tracker")
        self.parser.add_argument(
            "--add",
            dest="add",
            type=str,
            help="add task",
        )
        self.parser.add_argument(
            "--remove",
            dest="remove",
            type=int,
            help="remove task",
        )
        self.parser.add_argument(
            "--change-status",
            dest="change_status",
            type=int,
            help="change task status",
        )

        self.parser.add_argument(
            "--tasks",
            dest="tasks",
            action="store_true",
            help="list tasks",
        )
        self.parser.add_argument(
            "--completed",
            dest="completed",
            action="store_true",
            help="list completed tasks",
        )
        self.parser.add_argument(
            "--uncompleted",
            dest="uncompleted",
            action="store_true",
            help="list uncompleted tasks",
        )

        self.args = self.parser.parse_args()

    def handle_args(self):
        tracker = TaskTracker()

        actions = {
            "add": lambda: tracker.add_task(self.args.add),
            "remove": lambda: tracker.remove_task(self.args.remove),
            "change_status": lambda: tracker.change_status(
                self.args.change_status
            ),
            "tasks": tracker.list_tasks,
            "completed": tracker.list_completed_tasks,
            "uncompleted": tracker.list_uncompleted_tasks,
        }

        for action, func in actions.items():
            arg_value = getattr(self.args, action)
            if arg_value is not None:
                return func()

        print("Invalid command")
