words = list(input().split())
mandatoryDictionary = {}

# Converts the list into a string and gets rid of spaces
string = "".join(words)

def letterFrequency(letter, string):
    # NOTE: frequency is calculated by dividing count(letter) by len(string), rounded to 2 decimal places
    return round(string.count(letter) / len(string), 2)

uniqueString = "".join(sorted(set(string)))

for letter in uniqueString:
    # yoinks the letter and its frequency into a dictionary (because i'm supposed to use those for this exam, despite this being completely unnecessary lol)
    mandatoryDictionary[letter] = letterFrequency(letter, string)

for keys, values in mandatoryDictionary.items():
    print(f"{keys} - {values}")


# --- MORE IMPRACTICAL SOLUTION WITH MORE DICTIONARY USAGE (JUST IN CASE THIS WASN'T ENOUGH) ---
    
# words = list(input().split())
# mandatoryDictionary = {}

# string = "".join(words)
# def letterFrequency(letter, string):
#     return round(string.count(letter) / len(string), 2)
#
# uniqueString = "".join(sorted(set(string)))
# # counts the frequency of each letter in the string and adds it to the dictionary
# for letter in uniqueString:
#     mandatoryDictionary[letter] = letterFrequency(letter, string)
#
# for keys, values in mandatoryDictionary.items():
#     print(f"{keys} - {round(values/len(string), 2)}")
