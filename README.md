### CLI Task Tracker

The **CLI Task Tracker** is a command-line tool designed to help users manage their tasks efficiently through a lightweight, intuitive interface. Built with Python, this task tracker allows users to create, update, list, and delete tasks directly from the terminal. The tasks are stored locally in a JSON file, providing persistent storage without the need for a database.

#### Features:
- **Add Tasks**: Quickly add new tasks to your to-do list with the `--add` command.
- **Remove Tasks**: Delete tasks by specifying the task ID with the `--remove` command.
- **Change Task Status**: Mark tasks as completed or uncompleted with the `--change-status` command.
- **List Tasks**: View all tasks with the `--tasks` command.
- **Filter Tasks**: Display only completed or uncompleted tasks using the `--completed` or `--uncompleted` commands.

#### Usage:
```bash
# Add a task
python3 cli-task-tracker.py --add "Finish project documentation"

# Remove a task
python3 cli-task-tracker.py --remove 1

# Mark task as completed/uncompleted
python3 cli-task-tracker.py --change-status 0

# List all tasks
python3 cli-task-tracker.py --tasks

# List only completed tasks
python3 cli-task-tracker.py --completed

# List only uncompleted tasks
python3 cli-task-tracker.py --uncompleted
```

#### File Structure:
- **tasks.json**: Stores tasks and their statuses.
- **task_tracker.py**: Contains the core logic for managing tasks.
- **arg_parses.py**: Handles the CLI argument parsing.
- **cli-task-tracker**: Main executive file.

#### Getting Started:
1. Clone the repository:
    ```bash
    git clone https://github.com/Dedstate/CLI-Task-Tracker.git
    cd CLI-Task-Tracker
    ```

2. Run the script with desired commands to manage your tasks.

#### Contributions:
Feel free to fork the repository and submit pull requests to improve functionality, fix bugs, or add new features!

---

This simple, modular design can be easily extended and customized to fit different task management needs.

[CLI-Task-Tracker](https://roadmap.sh/projects/task-tracker)
