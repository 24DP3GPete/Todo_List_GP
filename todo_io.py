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
        tasks = []
        for row in reader:
            # Ensure date_added exists, set to "Before Time" if missing
            if 'date_added' not in row:
                row['date_added'] = "Before Time"
            tasks.append(row)
        return tasks


def save_tasks(tasks, task_file=None):
    path = _normalize_path(task_file)
    if not tasks:
        with open(path, "w", encoding="utf-8", newline='') as f:
            pass
        return
    fieldnames = ['nosaukums', 'description', 'priority', 'status', 'date_added']
    with open(path, "w", encoding="utf-8", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for task in tasks:
            writer.writerow(task)
