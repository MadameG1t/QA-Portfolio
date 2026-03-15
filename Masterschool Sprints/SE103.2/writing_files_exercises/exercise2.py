with open("olympic-medals.csv", "r") as infile, open("olympic-medals-short.csv", "w") as outfile:
    for i in range(10):
        line = infile.readline()
        outfile.write(line)