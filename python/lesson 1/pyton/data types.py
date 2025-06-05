def check(a):
    le = len(a)
    start = 0
    end = le - 1
    while start < end:
        if a[start] != a[end]:
            return False
        start += 1
        end -= 1
    return True

a = (1, 2, 3, 7, 2, 1)
res = check(a)

if res:
    print("the tuple is a palindrome")
else:
    print("the tuple is not a palindrome")
