import os

print ("Hi, I can save a new file with your name, address, and phone number, in a specified directory for you.")
userPath = input("Give me the path to the directory that you want to save the new file in: \n")
try:
    os.path.isdir(userPath)
    
except:
    print("Specified directory path does not exist.")
    quit()
newFile = input("What do you want to name the new file?\n")
filePath = os.path.join(userPath, newFile)
name = input("What's your name?\n")
address = input("What's your address?\n")
number = input("What's your phone number?\n")
try:    
    with open(filePath, 'w') as file_object: #create new file
        data = (name + ", " + address + ", " + number)
        file_object.write(data) #write to file
except:
    print("Error creating/writing to new file.")
    quit()
try:
    with open(filePath) as file_object:
        print("Today we created a new file, " + newFile + ", and we added the following information to the file: ")
        print(file_object.read())
except:
    print("Error reading file.")
    quit()