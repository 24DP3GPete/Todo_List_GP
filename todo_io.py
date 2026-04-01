import os

DEFAULT_JOB_FILE = "job.txt"


def _normalize_path(job_file):
    return job_file if job_file is not None else DEFAULT_JOB_FILE


def load_jobs(job_file=None):
    path = _normalize_path(job_file)
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f if line.strip()]


def save_jobs(jobs, job_file=None):
    path = _normalize_path(job_file)
    with open(path, "w", encoding="utf-8") as f:
        for item in jobs:
            f.write(item + "\n")
