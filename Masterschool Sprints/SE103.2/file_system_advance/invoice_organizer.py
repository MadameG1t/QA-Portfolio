import os
import shutil


def extract_month(filename):
    parts = filename.split("_")
    if len(parts) < 3:
        print(f"Skipping invalid filename: {filename}")
        return None
    return parts[2].split(".")[0]


parent_folder = os.getcwd()
invoices_folder = os.path.join(parent_folder, "invoices")

for filename in os.listdir(invoices_folder):

    if not filename.lower().endswith(".pdf"):
        continue

    month = extract_month(filename)


    if month is None:
        continue

    month_folder = os.path.join(invoices_folder, month)
    os.makedirs(month_folder, exist_ok=True)


    src = os.path.join(invoices_folder, filename)
    dst = os.path.join(month_folder, filename)
    shutil.move(src, dst)

    print(f"Moved: {filename} -> {month}/")
