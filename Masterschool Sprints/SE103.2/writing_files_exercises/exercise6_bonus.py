import csv

with open("olympic-medals.csv", "r", newline="") as infile:
    reader = csv.reader(infile)
    next(reader)  # skip header

    for row in reader:
        country = row[0]
        gold = int(row[1])
        silver = int(row[2])
        bronze = int(row[3])

        total = gold + silver + bronze

        with open(f"{country}.txt", "w") as outfile:
            outfile.write(str(total))