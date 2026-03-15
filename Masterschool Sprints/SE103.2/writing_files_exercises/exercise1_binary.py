with open("baseball.jpg", "rb") as infile:
    data = infile.read()

with open("baseball-copy.jpg", "wb") as outfile:
    outfile.write(data)