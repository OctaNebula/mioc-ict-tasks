encodedstring = input()

#As long as the string contains "apa", "epe", "ipi", "opo", or "upu" commit to the loop
while encodedstring.__contains__("apa") or encodedstring.__contains__("epe") or encodedstring.__contains__("ipi") or encodedstring.__contains__("opo") or encodedstring.__contains__("upu"):
    #Replaces "apa", "epe", "ipi", "opo", "upu" with their respective vowels
    encodedstring = encodedstring.replace("apa", "a")
    encodedstring = encodedstring.replace("epe", "e")
    encodedstring = encodedstring.replace("ipi", "i")
    encodedstring = encodedstring.replace("opo", "o")
    encodedstring = encodedstring.replace("upu", "u")
print(encodedstring)