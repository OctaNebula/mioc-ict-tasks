def vigenereEncrypt(string, key):
    string = string.upper()
    key = key.upper()
    encrypted = ""
    for i in string:
        if i.isalpha():
            encrypted += chr(((ord(i) + ord(key[0])) % 26) + 65)
            key += key[0]
        else:
            encrypted += i
    return encrypted

def vigenereDecrypt(string, key):
    string = string.upper()
    key = key.upper()
    for i in range(len(string)):
        key += key[0]
    decrypted = ""
    for i in string:
        if i.isalpha():
            decrypted += chr(((ord(i) - ord(key[0])) % 26) + 65)
        else:
            decrypted += i
    print(key)
    return decrypted

def vigenereEncryptAutoKey(string, key):
    key = key + string
    key = key[:len(string)]
    encrypted = ""
    for i in range(len(string)):
        encrypted += chr((ord(string[i]) + ord(key[i])) % 26 + 65)
    return encrypted

def vigenereDecryptAutoKey(string, key):
    decrypted = ""
    for i in range(len(string)):
        decrypted += chr((ord(string[i]) - ord(key[i])) % 26 + 65)
        key += decrypted[i]
    return decrypted



string = "TEOTKXRPNBUPFXFP"
key = "STOL"

vigenereDecrypt(string, key)