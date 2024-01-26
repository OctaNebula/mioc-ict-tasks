word = input()

# counts every letter in the word and stores it in a dictionary

counts = {}
for letter in word:
    if letter in counts:
        counts[letter] += 1 # if the letter is already in the dictionary, add 1 to its value
    else:
        counts[letter] = 1 # if the letter is not in the dictionary, add it and set its value to 1

# prints the ammount of letters that appear an 2 or more times
        
counter  = 0

for letter in counts:
    if counts[letter] >= 2: # if the letter appears 2 or more times, add 1 to the counter
        counter += 1

print(counter)