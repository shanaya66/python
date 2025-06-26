class employee:
    def __init__(self):
        print("employee created")

    def __del__(self):
        print("employee deleted")

e1 = employee()
print("In the middle")
del e1