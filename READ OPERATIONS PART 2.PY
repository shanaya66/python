# file operations
print("the entire content of the file")
file1 = open("codingalupdated1.txt","r")
print(file1.read())
file1.close()

# write mode
file1 = open("codingalupdated1.txt","w")
print(file1.write("I am wrriting this file"))
file1.close()

# append mode
print("\n append name and age")
file3 = open("codingalupdated1.txt","a")
file3.write("name = 'Codingal \n age = 6 years old'")
file3.close()
