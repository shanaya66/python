#program to find the element not making  a pair
#function to calculate the number that is odd occurring
def oddoccurring(arr):
    #initialize result
    res=0
    for element in arr:
        res=res^element
    return res
arr=[]
n=int(input("enter the array size"))
while n:
    num=int(input("enter number"))
    arr.append(num)
    n-=1
print("odd occurring is",oddoccurring(arr))