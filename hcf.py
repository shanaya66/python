# highest common Factor (HCF)

l = int(input("enter the largest number"))
s = int(input("enter the smallest number"))
print(f"the HCF of the {l} and {s} is", end = " ")
while s:
    t = s
    s = l%s
    l = t

print(l)
