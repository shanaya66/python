# file operations
print("the entire content of the file")
file1 = open("Codingal.txt", "r")
print(file1.read())
file1.close()

print("\nthe first eight characters")
file1 = open("Codingal.txt", "r")
print(file1.read(8))
file1.close()

print("\n append name and age")
file3 = open("Codingal.txt", "a")
file3.write("name = Codingal \n age = 6 years old")
file3.close()
