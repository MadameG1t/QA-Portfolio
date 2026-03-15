with open("olympic-medals.csv", "r") as infile:
    data = infile.read()

with open("olympic-medals-copy.csv", "w") as outfile:
    outfile.write(data)