import os
import shutil


def extract_month(filename: str) -> str | None:
    parts = filename.split("_")
    if len(parts) < 3:
        print(f"Skipping invalid filename: {filename}")
        return None
    return parts[2].split(".")[0]


def make_folder(path: str) -> None:
    if not os.path.exists(path):
        os.mkdir(path)


def move_to_month_folder(file_path: str, month: str, invoices_folder: str) -> None:
    filename = os.path.basename(file_path)
    destination_path = os.path.join(invoices_folder, month, filename)
    shutil.move(file_path, destination_path)



parent_folder = os.getcwd()
invoices_folder = os.path.join(parent_folder, "invoices")

print("Organizing invoices...\n")

for entry in os.listdir(invoices_folder):
    entry_path = os.path.join(invoices_folder, entry)


    if os.path.isfile(entry_path) and entry.lower().endswith(".pdf"):
        month = extract_month(entry)
        if month is None:
            continue

        month_folder = os.path.join(invoices_folder, month)
        make_folder(month_folder)

        move_to_month_folder(entry_path, month, invoices_folder)
        print(f"Moved: {entry} -> {month}/")


    elif os.path.isdir(entry_path):
        for filename in os.listdir(entry_path):
            file_path = os.path.join(entry_path, filename)

            if not (os.path.isfile(file_path) and filename.lower().endswith(".pdf")):
                continue

            month = extract_month(filename)
            if month is None:
                continue

            month_folder = os.path.join(invoices_folder, month)
            make_folder(month_folder)

            move_to_month_folder(file_path, month, invoices_folder)
            print(f"Moved: {filename} -> {month}/")

