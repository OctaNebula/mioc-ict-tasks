name = input()

#replaces -s with spaces
name = name.replace("-"," ")

#splits the string into a list of words
name = name.split()
print(name[1])