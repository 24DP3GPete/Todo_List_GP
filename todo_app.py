from todo_io import load_job, save_job


def show_job(job):
    if not job:
        print("No job yet. Add one!")
        return

    print("\nYour job list:")
    for i, item in enumerate(job, start=1):
        print(f"{i}. {item}")
    print()


def add_job(job, job_file=None):
    item = input("Enter new job: ").strip()
    if not item:
        print("Empty job not added.")
        return job

    job.append(item)
    save_job(job, job_file=job_file or None)
    print("Added:", item)
    return job


def remove_job(job, job_file=None):
    if not job:
        print("Nothing to remove.")
        return job

    show_job(job)
    val = input("Enter number to remove (or press Enter to cancel): ").strip()
    if not val:
        print("Canceled.")
        return job

    if not val.isdigit():
        print("Please enter a valid number.")
        return job

    idx = int(val) - 1
    if idx < 0 or idx >= len(job):
        print("Index out of range.")
        return job

    removed = job.pop(idx)
    save_job(job, job_file=job_file or None)
    print("Removed:", removed)
    return job
