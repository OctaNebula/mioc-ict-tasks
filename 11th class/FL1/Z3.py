mainFile = open("zadatak3a.txt", "r")

rows = []

# Appends each row to the list
for row in mainFile:
    rows.append(row.strip())

# Splits each row into a list of integers
rows = [i.split(" ") for i in rows]

# Removes empty strings from the list
rows = [[i for i in j if i] for j in rows]

rows = [[int(j) for j in i] for i in rows]

sumList = [sum(i) for i in rows]

output = open("output3.txt", "w")

# Writes the sum of each row to the output file in a new line
for i in sumList:
    output.write(f"{i}\n")