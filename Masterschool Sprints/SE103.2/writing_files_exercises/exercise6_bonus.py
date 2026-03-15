import csv
import os

print(os.getcwd())

with open("olympic-medals.csv", "r", newline="") as infile:
    reader = csv.reader(infile)
    next(reader)

    for row in reader:
        if len(row) < 5:
            continue

        country = row[1].strip()
        gold = int(row[2])
        silver = int(row[3])
        bronze = int(row[4])

        total = gold + silver + bronze

        with open(f"{country}.txt", "w") as outfile:
            outfile.write(str(total))