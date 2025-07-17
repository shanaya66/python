# Opening and reading the file using 'with' (auto-closes file)
with open("codingal.txt", "r") as file1:
    content = file1.read()
    print(content)
