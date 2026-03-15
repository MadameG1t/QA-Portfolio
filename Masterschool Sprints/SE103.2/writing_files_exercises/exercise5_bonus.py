with open("olympic-medals.csv", "r") as infile, open("olympic-medals-total10.csv", "w") as outfile:
    header = infile.readline()
    outfile.write(header)

    for line in infile:
        parts = line.strip().split(",")

        if len(parts) < 5:
            continue

        gold = int(parts[2])
        silver = int(parts[3])
        bronze = int(parts[4])

        total = gold + silver + bronze

        if total >= 10:
            outfile.write(line)