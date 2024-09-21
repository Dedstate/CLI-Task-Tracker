import unittest
from unittest.mock import patch, mock_open
from task_tracker.task_tracker import TaskTracker


class TestTaskTracker(unittest.TestCase):

    @patch("pathlib.Path.exists", return_value=True)
    @patch("pathlib.Path.open", new_callable=mock_open, read_data="[]")
    def test_add_task(self, mock_file, mock_exists):
        tracker = TaskTracker()
        tracker.add_task("Test task")

        mock_file.assert_called_with("w")
        self.assertEqual(tracker.index, 1)

    @patch("pathlib.Path.exists", return_value=True)
    @patch(
        "pathlib.Path.open",
        new_callable=mock_open,
        read_data='[{"id": 0, "task": "Test task", "status": "[_]"}]',
    )
    def test_remove_task(self, mock_file, mock_exists):
        tracker = TaskTracker()
        tracker.remove_task(0)

        mock_file.assert_called_with("w")

    @patch("pathlib.Path.exists", return_value=True)
    @patch(
        "pathlib.Path.open",
        new_callable=mock_open,
        read_data='[{"id": 0, "task": "Test task", "status": "[_]"}]',
    )
    def test_change_status(self, mock_file, mock_exists):
        tracker = TaskTracker()
        tracker.change_status(0)

        mock_file.assert_called_with("w")


if __name__ == "__main__":
    unittest.main()
