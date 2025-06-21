class parrot:
    species = "Maccaw"
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = parrot("rubix",3)
p2 = parrot("Barnie",2)

print("my name is",p1.name,'my age is',p1.age)
print("my name is",p2.name,'my age is',p2.age)
