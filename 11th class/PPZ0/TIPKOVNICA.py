# WARNING: YANDERE DEV CODE AHEAD

typoedWord = input()

samples = int(input())
wordlist = []

for i in range(samples):

    word = input()
    lenght = 0
    if len(word) == len(typoedWord):
        for i in word:
            test = True # the test variable is certified 100% useless because when i realized it's broken it was far too late due to this is yanderedev simulator 2019
        
            if typoedWord[lenght] == "A": # passes if i == "A" or Q, W, S or Z
                if i in ["A", "Q", "W", "S", "Z"]:
                    break
                else:
                    test = False
                    break
            elif typoedWord[lenght] == "B":
                if i in ["B", "V", "G", "H", "N"]:
                    break
                else:
                    test = False
                    break
            elif typoedWord[lenght] == "C":
                if i in ["C", "X", "D", "F", "V"]:
                    break
                else:
                    test = False
                    break
            elif typoedWord[lenght] == "D":
                if i in ["D", "S", "E", "R", "F", "C", "X"]:
                    break
                else:
                    test = False
                    break
            elif typoedWord[lenght] == "E":
                if i in ["E", "W", "S", "D", "R"]:
                    break
                else:
                    test = False
                    break
            elif typoedWord[lenght] == "F":
                if i in ["F", "D", "R", "T", "G", "V", "C"]:
                    break
                else:
                    test = False
                    break
            elif typoedWord[lenght] == "G":
                if i in ["G", "F", "T", "Y", "H", "B", "V"]:
                    break
                else:
                    test = False
                    break
            elif typoedWord[lenght] == "H":
                if i in ["H", "G", "Y", "U", "J", "N", "B"]:
                    break
                else:
                    test = False
                    break
            elif typoedWord[lenght] == "I":
                if i in ["I", "U", "J", "K", "O"]:
                    break
                else:
                    test = False
                    break
            elif typoedWord[lenght] == "J":
                if i in ["J", "H", "U", "I", "K", "M", "N"]:
                    break
                else:
                    test = False
                    break
            elif typoedWord[lenght] == "K":
                if i in ["K", "J", "I", "O", "L", "M"]:
                    break
                else:
                    test = False
                    break
            elif typoedWord[lenght] == "L":
                if i in ["L", "K", "O", "P"]:
                    break
                else:
                    test = False
                    break
            elif typoedWord[lenght] == "M":
                if i in ["M", "N", "J", "K"]:
                    break
                else:
                    test = False
                    break
            elif typoedWord[lenght] == "N":
                if i in ["N", "B", "H", "J", "M"]:
                    break
                else:
                    test = False
                    break
            elif typoedWord[lenght] == "O":
                if i in ["O", "I", "K", "L", "P"]:
                    break
                else:
                    test = False
                    break
            elif typoedWord[lenght] == "P":
                if i in ["P", "O", "L"]:
                    break
                else:
                    test = False
                    break
            elif typoedWord[lenght] == "Q":
                if i in ["Q", "A", "W"]:
                    break
                else:
                    test = False
                    break
            elif typoedWord[lenght] == "R":
                if i in ["R", "E", "D", "F", "T"]:
                    break
                else:
                    test = False
                    break
            elif typoedWord[lenght] == "S":
                if i in ["S", "A", "W", "E", "D", "X", "Z"]:
                    break
                else:
                    test = False
                    break
            elif typoedWord[lenght] == "T":
                if i in ["T", "R", "F", "G", "Y"]:
                    break
                else:
                    test = False
                    break
            elif typoedWord[lenght] == "U":
                if i in ["U", "Y", "H", "J", "I"]:
                    break
                else:
                    test = False
                    break
            elif typoedWord[lenght] == "V":
                if i in ["V", "C", "F", "G", "B"]:
                    break
                else:
                    test = False
                    break
            elif typoedWord[lenght] == "W":
                if i in ["W", "Q", "A", "S", "E"]:
                    break
                else:
                    test = False
                    break
            elif typoedWord[lenght] == "X":
                if i in ["X", "Z", "S", "D", "C"]:
                    break
                else:
                    test = False
                    break
            elif typoedWord[lenght] == "Y":
                if i in ["Y", "T", "G", "H", "U"]:
                    break
                else:
                    test = False
                    break
            elif typoedWord[lenght] == "Z":
                if i in ["Z", "A", "S", "X"]:
                    break
                else:
                    test = False
                    break
            lenght += 1
    
    if test:
        wordlist.append(word)
wordlist.sort()
for i in wordlist:
    print(i)
