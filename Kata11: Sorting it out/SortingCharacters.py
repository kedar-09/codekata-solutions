import re
str = "When not studying nuclear physics, Bambi likes to play beach volleyball."
print(str)
#STRING CONVERSION (one string with all lowercase, no commas, fullstops and no blankspaces).
#string = re.sub('[^A-Za-z]','',string)         #this removes all the spaces full stops and commas.
str = re.sub('[^A-Za-z]','',str).lower()        #this removes spaces, and makes all capital letters small, because of lower().
print(str)
#convert string to list to iterate
liststring=list(str)
#print(liststring)
#store the length of the list in a variable
lenlist=len(liststring)
print(lenlist)

#bubble sort
for i in range(lenlist-1):
    for j in range(lenlist-i-1):
        if liststring[j]>liststring[j+1]:
          liststring[j],liststring[j+1]=liststring[j+1],liststring[j]

#convert list to string again
def listToString(s):
    str1=""
    return(str1.join(s))


# print the string (sorted alphabets)
print(listToString(liststring))
