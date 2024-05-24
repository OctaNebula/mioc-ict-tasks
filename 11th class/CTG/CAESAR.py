commonBigrams = ["TH", "HE", "IN", "ER", "AN", "RE"]

def caesar_encrypt(string, shift):
    encrypted_string = ""
    string = string.upper()
    for char in string:
        if char.isalpha():
            ascii_val = ord(char) + shift
            if ascii_val > ord("Z"):
                ascii_val -= 26
            elif ascii_val < ord("A"):
                ascii_val += 26
            encrypted_string += chr(ascii_val)
        else:
            encrypted_string += char
    return encrypted_string

def caesar_decrypt(string, bigrams, reqScore):
    score = 0
    string = string.upper()
    for shift in range(26):
        decrypted_string = caesar_encrypt(string, -shift)
        for bigram in bigrams:
            score += decrypted_string.count(bigram)
        if score >= reqScore:
            return decrypted_string
    return "Decryption failed"

def caesar_decrypt_knownKey(string, shift):
    return caesar_encrypt(string, -shift)

caesar_decrypt("nbyzcnhymmalugjuwylnymncmugofncmnuayuylivcwwujuwcnsnymn", commonBigrams, 15)