#program to swap two numbers without using 3rd variable 

def swap1(a,b):
    #code to swap a and b
    a=a^b
    b=a^b
    a=a^b
    print ("after swaping:a=",a,"b=",b)
swap1(23,45)
 
def swap2(a,b):
   a=(a&b)+(a|b)
   b=a+(~b)+1
   a=a+(~b)+1

   print("after swaping:a=",a,"b=",b)
swap2(24,56)
    