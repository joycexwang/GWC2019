#Opens a file. You can now look at each line in the file individually with a statement like "for line in f:
f = open("dictionary.txt","r")
#print(type(f))
print("Can your password survive a dictionary attack?")

#Take input from the keyboard, storing in the variable test_password
#NOTE - You will have to use .strip() to strip whitespace and newlines from the file and passwords
test_password= input("Type in a trial password: ").lower()
extraList = ["0", "1"]
#Write logic to see if the password is in the dictionary file below here:

for word in f:
#    if test_password.strip() == word.strip():
        #print("bad password")
    #if len(test_password).strip() < 3:
        #print("too short")
    #if len(test_password) == 3:
        #print("short")
    if test_password.strip() != word.strip():
        continue
#    if test_password.strip() == word.strip() + extraList():
#        print("haha")
    else:
        print("that is a bad password")
