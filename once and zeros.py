#program to find the number of zero bits and one bits present in a number
#functions taking our number as input
def numberofbits(n):
    ones=0
    zeros=0
    #while our number is greater than zero check last bit and right shift
    while(n):
        #use and operator to check if last bit is one or zero
        if(n&1==1):
            ones+=1
        else:
            zeros+=1
        #right shift the number remove the last bit that we just checked above
        n>>=1
    print("ones=",ones,"zeros=",zeros)
number = int(input("enter youre number"))
numberofbits(number)