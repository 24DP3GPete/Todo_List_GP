import os
import csv

DEFAULT_TASK_FILE = "task.csv"


def _normalize_path(task_file):
    return task_file if task_file is not None else DEFAULT_TASK_FILE


def load_tasks(task_file=None):
    path = _normalize_path(task_file)
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8", newline='') as f:
        reader = csv.DictReader(f)
        return list(reader)


def save_tasks(tasks, task_file=None):
    path = _normalize_path(task_file)
    if not tasks:
        # If no tasks, just create empty file or remove?
        with open(path, "w", encoding="utf-8", newline='') as f:
            pass
        return
    fieldnames = ['nosaukums', 'description', 'priority', 'status']
    with open(path, "w", encoding="utf-8", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for task in tasks:
            writer.writerow(task)
