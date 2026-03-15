with open("olympic-medals.csv", "r") as infile, open("olympic-medals-5.csv", "w") as outfile:
    header = infile.readline()
    outfile.write(header)

    for line in infile:
        parts = line.strip().split(",")

        gold = int(parts[1])

        if gold >= 5:
            outfile.write(line)