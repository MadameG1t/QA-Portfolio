with open("baseball.jpg", "rb") as infile:
    data = infile.read()

with open("baseball-part.jpg", "wb") as outfile:
    outfile.write(data[:30000])