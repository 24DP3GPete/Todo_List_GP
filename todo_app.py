from todo_io import load_jobs, save_jobs


def show_jobs(job):
    if not job:
        print("Vēl nav darbu. Pievienojiet vienu!")
        return

    print("\nJūsu darbu saraksts:")
    for i, item in enumerate(job, start=1):
        print(f"{i}. {item}")
    print()


def add_job(job, job_file=None):
    item = input("Ievadiet jaunu darbu: ").strip()
    if not item:
        print("Tukšs darbs nav pievienots.")
        return job

    job.append(item)
    save_jobs(job, job_file=job_file or None)
    print("Pievienots:", item)
    return job


def remove_job(job, job_file=None):
    if not job:
        print("Nav ko noņemt.")
        return job

    show_jobs(job)
    val = input("Ievadiet numuru, lai noņemtu (vai nospiediet Enter, lai atceltu): ").strip()
    if not val:
        print("Atcelts.")
        return job

    if not val.isdigit():
        print("Lūdzu ievadiet derīgu numuru.")
        return job

    idx = int(val) - 1
    if idx < 0 or idx >= len(job):
        print("Indekss ārpus diapazona.")
        return job

    removed = job.pop(idx)
    save_jobs(job, job_file=job_file or None)
    print("Noņemts:", removed)
    return job


def edit_job(job, job_file=None):
    if not job:
        print("Nav ko rediģēt.")
        return job

    show_jobs(job)
    val = input("Ievadiet numuru, lai rediģētu (vai nospiediet Enter, lai atceltu): ").strip()
    if not val:
        print("Atcelts.")
        return job

    if not val.isdigit():
        print("Lūdzu ievadiet derīgu numuru.")
        return job

    idx = int(val) - 1
    if idx < 0 or idx >= len(job):
        print("Indekss ārpus diapazona.")
        return job

    old_item = job[idx]
    new_item = input(f"Rediģējiet '{old_item}' uz: ").strip()
    if not new_item:
        print("Tukšs rediģējums nav saglabāts.")
        return job

    job[idx] = new_item
    save_jobs(job, job_file=job_file or None)
    print("Rediģēts:", old_item, "->", new_item)
    return job