with open("olympic-medals.csv", "r") as infile:
    header = infile.readline()

    for line in infile:
        parts = line.strip().split(",")

        if len(parts) < 5:
            continue

        country = parts[1].replace('"', '')

        gold = int(parts[2])
        silver = int(parts[3])
        bronze = int(parts[4])

        total = gold + silver + bronze

        filename = f"{country}.txt"

        with open(filename, "w") as outfile:
            outfile.write(str(total))