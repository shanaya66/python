class library:
    booklist = []

    def __init__(self, list):
        self.booklist = list
        self.lendbooklist = []

    def addbooks(self, bname):
        self.booklist.append(bname)
        print("books added")

    def displaybooks(self):
        print("the list of books are")
        for i in self.booklist:
            print(i)

    def lendbooks(self, bname):
        if bname in self.booklist:
            self.lendbooklist.append(bname)
            self.booklist.remove(bname)
            print(bname, "lended to you")
        else:
            if bname in self.lendbooklist:
                print("Book already lended")
            else:
                print("Book not in the Library")

    def returnbooks(self, bname):
        if bname in self.lendbooklist:
            self.lendbooklist.remove(bname)


print("***Welcome to Chennai Library***")
print("Library Management system")

books = list(['Python', 'Harry porter', 'C++ Basics', 'Geronimo stilton', "Computer Visualization"])

L1 = library(books)
while True:

    ch = input("\n1.Add books \n2.Lend books \n3.Return books \n4.Display books \nenter your choice")
    if ch == "1":
        bookn = input("enter the name")
        L1.addbooks(bookn)
    elif ch == "2":
        bookn = input("enter the name")
        L1.lendbooks(bookn)
    elif ch == "3":
        bookn = input("enter the name")
        L1.returnbooks(bookn)
    elif ch == "4":
        print("display books")
        L1.displaybooks()
    choice = input("enter you want to quit (Y/N)")
    if choice.lower() == 'y':
        break