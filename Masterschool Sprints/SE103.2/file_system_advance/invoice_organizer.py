import os


parent_folder = os.getcwd()


invoices_folder = os.path.join(parent_folder, "invoices")


print("Contents of invoices folder:\n")

for item in os.listdir(invoices_folder):
    print(item)

