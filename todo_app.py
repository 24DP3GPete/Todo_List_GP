from todo_io import load_tasks, save_tasks


def show_tasks(task, title=None):
    if not task:
        print("Vēl nav darbu. Pievienojiet vienu!")
        return

    if title:
        print(f"\n{title}")
    else:
        print("\nUzdevumu saraksts:")
    for i, item in enumerate(task, start=1):
        print(f"{i}. {item['nosaukums']}")
    print()


def filter_tasks(task):
    if not task:
        print("Nav uzdevumu.")
        return

    fields = {
        "1": ("nosaukums", "Nosaukums"),
        "2": ("description", "Apraksts"),
        "3": ("priority", "Prioritāte"),
        "4": ("status", "Statuss")
    }

    print("\nFiltrēt pēc:")
    for key, (_, label) in fields.items():
        print(f"{key}) {label}")

    field_choice = input("Izvēlieties lauku: ").strip()
    if field_choice not in fields:
        print("Nederīga izvēle.")
        return

    field_key, field_label = fields[field_choice]

    filter_value = input(f"Ievadiet meklējamo {field_label} tekstu: ").strip()
    if not filter_value:
        print("Atcelts.")
        return

    search_text = filter_value.lower()
    filtered = [item for item in task if search_text in item.get(field_key, "").lower()]
    if not filtered:
        print("Nav uzdevumu, kas atbilst izvēlētajam filtram.")
        return

    show_tasks(filtered, title=f"Uzdevumi ar {field_label} satur '{filter_value}'")


def view_details(task):
    if not task:
        print("Nav uzdevumu.")
        return

    show_tasks(task)
    val = input("Ievadiet numuru, lai skatītu detaļas (vai Enter, lai atceltu): ").strip()
    if not val:
        print("Atcelts.")
        return

    if not val.isdigit():
        print("Lūdzu ievadiet derīgu numuru.")
        return

    idx = int(val) - 1
    if idx < 0 or idx >= len(task):
        print("Indekss ārpus diapazona.")
        return

    item = task[idx]
    print("\nDetaļas:")
    print(f"Nosaukums: {item['nosaukums']}")
    print(f"Apraksts: {item['description']}")
    print(f"Prioritāte: {item['priority']}")
    print(f"Statuss: {item['status']}")
    print()


def add_task(task, task_file=None):
    nosaukums = input("Ievadiet nosaukumu: ").strip()
    if not nosaukums:
        print("Tukšs nosaukums nav pievienots.")
        return task

    description = input("Ievadiet aprakstu: ").strip()
    priority = input("Ievadiet prioritāti (zems/vidējs/augsts): ").strip()
    status = input("Ievadiet statusu (gaida/darbojas/pabeigts): ").strip()

    new_task = {
        'nosaukums': nosaukums,
        'description': description,
        'priority': priority,
        'status': status
    }

    task.append(new_task)
    save_tasks(task, task_file=task_file or None)
    print("Pievienots:", nosaukums)
    return task


def remove_task(task, task_file=None):
    if not task:
        print("Nav ko noņemt.")
        return task

    show_tasks(task)
    val = input("Ievadiet numuru, lai noņemtu (vai nospiediet Enter, lai atceltu): ").strip()
    if not val:
        print("Atcelts.")
        return task

    if not val.isdigit():
        print("Lūdzu ievadiet derīgu numuru.")
        return task

    idx = int(val) - 1
    if idx < 0 or idx >= len(task):
        print("Indekss ārpus diapazona.")
        return task

    removed = task.pop(idx)
    save_tasks(task, task_file=task_file or None)
    print("Noņemts:", removed['nosaukums'])
    return task


def edit_task(task, task_file=None):
    if not task:
        print("Nav ko rediģēt.")
        return task

    show_tasks(task)
    val = input("Ievadiet numuru, lai rediģētu (vai nospiediet Enter, lai atceltu): ").strip()
    if not val:
        print("Atcelts.")
        return task

    if not val.isdigit():
        print("Lūdzu ievadiet derīgu numuru.")
        return task

    idx = int(val) - 1
    if idx < 0 or idx >= len(task):
        print("Indekss ārpus diapazona.")
        return task

    current = task[idx]
    print(f"Rediģējat: {current['nosaukums']}")

    new_nosaukums = input(f"Nosaukums ({current['nosaukums']}): ").strip() or current['nosaukums']
    new_description = input(f"Apraksts ({current['description']}): ").strip() or current['description']
    new_priority = input(f"Prioritāte ({current['priority']}): ").strip() or current['priority']
    new_status = input(f"Statuss ({current['status']}): ").strip() or current['status']

    task[idx] = {
        'nosaukums': new_nosaukums,
        'description': new_description,
        'priority': new_priority,
        'status': new_status
    }

    save_tasks(task, task_file=task_file or None)
    print("Rediģēts.")
    return task