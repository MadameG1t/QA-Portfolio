import os
import shutil


def extract_month(filename):
    parts = filename.split("_")
    if len(parts) < 3:
        print(f"Skipping invalid filename: {filename}")
        return None
    return parts[2].split(".")[0]


def make_folder(path):
    if not os.path.exists(path):
        os.mkdir(path)
        print(f"Created folder: {path}")

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

    source = os.path.join(invoices_folder, filename)
    destination = os.path.join(month_folder, filename)

    shutil.move(source, destination)

    print(f"Moved: {filename} -> {month}/")

