from todo_app import load_jobs, show_jobs, add_job, remove_job


if __name__ == "__main__":
    def main(job_file=None):
        file_path = job_file or None
        jobs = load_jobs(job_file=file_path)

        while True:
            print("\njob Menu:\n1) List jobs\n2) Add job\n3) Remove job\n4) Quit")
            choice = input("Choose an option: ").strip()

            if choice == "1":
                show_jobs(jobs)
            elif choice == "2":
                jobs = add_job(jobs, job_file=file_path)
            elif choice == "3":
                jobs = remove_job(jobs, job_file=file_path)
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid choice; please enter 1-4.")

