email = input()
#gets rid of all spaces
email = email.replace(" ","")
#deletes everything after @
email = email[:email.find("@")]
email = email.replace("@","")
#replaces dot with space
email = email.replace("."," ")
print(email)