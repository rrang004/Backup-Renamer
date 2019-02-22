#This script was created to aid me in renaming instrument stem files by removing the backup date and time
#Wanna delete 25 characters, from ( to )
import os

#os.listdir(os.curdir)
print("backup renamer 2000 v1")
for filename in os.listdir("."):
    print(filename)
    curName = filename
    print("curName = " + curName)
    newName = [] #we use a list to build the string but we will convert it to a real string once we are done
    parensFlag = False
    for c in curName: #iterate through the current file so we can find and create a new name
        print(c)
        if c == "(":
            newName = newName[:-1] #remove the space by splicing
            print("setting parensFlag to true")
            parensFlag = True
            continue
        if c == ")":
            print("setting parensFlag to false")
            parensFlag = False
            continue
        if not parensFlag:
            newName.append(c)
    newNameStr = ''.join(newName)
    print("newName = " + newNameStr)
    os.rename(curName, newNameStr)