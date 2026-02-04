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
        print(f"Created folder: {path}")


def move_to_month_folder(filename: str, month: str, invoices_folder: str) -> None:
    source_path = os.path.join(invoices_folder, filename)
    destination_path = os.path.join(invoices_folder, month, filename)

    shutil.move(source_path, destination_path)


parent_folder = os.getcwd()
invoices_folder = os.path.join(parent_folder, "invoices")

print("Organizing invoices...\n")

for filename in os.listdir(invoices_folder):


    if not filename.lower().endswith(".pdf"):
        continue


    month = extract_month(filename)

    if month is None:
        continue


    month_folder = os.path.join(invoices_folder, month)
    make_folder(month_folder)


    move_to_month_folder(filename, month, invoices_folder)

    print(f"Moved: {filename} -> {month}/")


