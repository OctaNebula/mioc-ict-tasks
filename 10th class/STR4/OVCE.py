gamelistchange = []
game = input()
#Splits the string into a list of strings, ex. OV#OOV#VOV becomes ["OV", "OOV", "VOV"]
gamelist = game.split("#")
#removes any empty strings from the list
while gamelist.__contains__(""): gamelist.remove("")

for i in gamelist:

    #If there is more sheep than wolves the sheep scare the wolves away (removes all wolves from the string)
    if i.count("O") > i.count("V"):
        i = i.replace('V', "")
        gamelistchange.append(i)
    #Otherwise, the sheep get eaten (removes all sheep from the string)
    else:
        i = i.replace('O', "")
        gamelistchange.append(i)

#reconstructs the string with the "#" in between, start and end of the string
print('''#{gamelistchange}#'''.format(gamelistchange="#".join(gamelistchange)))
