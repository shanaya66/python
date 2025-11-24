#programm to find power set of a set
import math
def printpowerset(set,setsize):
    powersetsize=(int)(math.pow(2,setsize))#find total elements possible in the power set
    outer=0
    inner=0
    for outer in range (0,powersetsize):
        for inner in range(0,setsize):
            #check if inner bit in the outer is set if setthen print the inner element from the set
            if ((outer & (1<<inner))>>0):
                print(set[inner],end="")
        print("")
size=int(input("enter the array size"))
set=[]
for i in range (0,size):
    n=int(input("enter the element"))
    set.append(n)
printpowerset(set,len(set))