wordsfile = open('Ulaz2.txt', 'r')
wordslist = []

# skip the first line when reading from the file
keys = wordsfile.readline().split()

for line in wordsfile:
    words = (line.strip()).split()
    for i in words:
        wordslist.append(i)

correspondingWords = []

for i in wordslist:
    for j in keys:
        if j in i and i not in correspondingWords:
            correspondingWords.append(i)

output = open('Izlaz2.txt', 'w')
for i in correspondingWords:
    output.write(i + '\n')
output.close()