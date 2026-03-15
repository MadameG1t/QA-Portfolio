with open("sample.mp3", "rb") as infile:
    data = infile.read()

with open("sample-twice.mp3", "wb") as outfile:
    outfile.write(data + data)