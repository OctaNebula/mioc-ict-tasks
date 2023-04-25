email = input()
#gets rid of all spaces
email = email.replace(" ","")
#deletes everything before @
email = email[email.find("@")+1:]
email = email.replace("@","")

if email == "skole.hr":
    print("DA skole")
else:
    #deletes the dot and everything after it
    emailnodot = email[:email.find(".")]
    print("NE {emailnodot}".format(emailnodot=emailnodot))