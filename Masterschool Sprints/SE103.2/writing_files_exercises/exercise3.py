with open("olympic-medals.csv", "r") as infile, open("olympic-medals-n.csv", "w") as outfile:
    header = infile.readline()
    outfile.write(header)

    for line in infile:
        if line.startswith("N"):
            outfile.write(line)