file1 = open("codingalupdated.txt", "r")
print(file1.read())
file1.close()

file2 = open("codingalupdated.txt", "w")
file2.write("I am learning coding\nI am learning file handling in python")
file2.close()

file1 = open("codingalupdated.txt", "r")
print(file1.read())
file1.close()

file2 = open("codingalupdated.txt", "a")
file2.write("This is easiest module in python")
file2.close()

file1 = open("codingalupdated.txt", "r")
print(file1.read())
file1.close()