from todo_app import load_jobs, show_jobs, add_job, remove_job, edit_job


if __name__ == "__main__":
    def main(job_file=None):
        file_path = job_file or None
        jobs = load_jobs(job_file=file_path)

        while True:
            print("\nMenu:\n1) Uzdevumu saraksts\n2) Pievienot uzdevumu\n3) Rediģēt uzdevumu\n4) Noņemt uzdevumu\n5) Iziet")
            choice = input("Izvēlēties opciju: ").strip()

            if choice == "1":
                show_jobs(jobs)
            elif choice == "2":
                jobs = add_job(jobs, job_file=file_path)
            elif choice == "3":
                jobs = edit_job(jobs, job_file=file_path)
            elif choice == "4":
                jobs = remove_job(jobs, job_file=file_path)
            elif choice == "5":
                break
            else:
                print("Nepareiza izvēle; lūdzu, ievadiet 1-5.")

    main()