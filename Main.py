from todo_app import load_tasks, show_tasks, filter_tasks, add_task, remove_task, edit_task, view_details


if __name__ == "__main__":
    def main(task_file=None):
        file_path = task_file or None
        tasks = load_tasks(task_file=file_path)

        while True:
            print("\nMenu:\n1) Skatīt uzdevumus\n2) Meklēt uzdevumus\n3) Skatīt uzdevumu detaļas\n4) Pievienot uzdevumu\n5) Rediģēt uzdevumu\n6) Noņemt uzdevumu\n7) Iziet")
            choice = input("Izvēlēties opciju: ").strip()

            if choice == "1":
                show_tasks(tasks)
            elif choice == "2":
                filter_tasks(tasks)
            elif choice == "3":
                view_details(tasks)
            elif choice == "4":
                tasks = add_task(tasks, task_file=file_path)
            elif choice == "5":
                tasks = edit_task(tasks, task_file=file_path)
            elif choice == "6":
                tasks = remove_task(tasks, task_file=file_path)
            elif choice == "7":
                break
            else:
                print("Nepareiza izvēle; lūdzu, ievadiet 1-7.")

    main()