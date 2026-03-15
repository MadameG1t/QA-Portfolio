with open("olympic-medals.csv", "r") as infile, open("olympic-medals-total10.csv", "w") as outfile:
    header = infile.readline()
    outfile.write(header)

    for line in infile:
        parts = line.strip().split(",")

        gold = int(parts[1])
        silver = int(parts[2])
        bronze = int(parts[3])

        total = gold + silver + bronze

        if total >= 10:
            outfile.write(line)