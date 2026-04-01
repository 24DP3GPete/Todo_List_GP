from todo_app import load_tasks, show_tasks, add_task, remove_task, edit_task, view_details


if __name__ == "__main__":
    def main(task_file=None):
        file_path = task_file or None
        tasks = load_tasks(task_file=file_path)

        while True:
            print("\nMenu:\n1) Skatīt uzdevumus\n2) Skatīt uzdevumu detaļas\n3) Pievienot uzdevumu\n4) Rediģēt uzdevumu\n5) Noņemt uzdevumu\n6) Iziet")
            choice = input("Izvēlēties opciju: ").strip()

            if choice == "1":
                show_tasks(tasks)
            elif choice == "2":
                view_details(tasks)
            elif choice == "3":
                tasks = add_task(tasks, task_file=file_path)
            elif choice == "4":
                tasks = edit_task(tasks, task_file=file_path)
            elif choice == "5":
                tasks = remove_task(tasks, task_file=file_path)
            elif choice == "6":
                break
            else:
                print("Nepareiza izvēle; lūdzu, ievadiet 1-6.")

    main()