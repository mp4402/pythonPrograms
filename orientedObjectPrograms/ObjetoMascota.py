class Pet:
    def __init__(self,name,age,hungry,walk):
        self.name = name
        self.age = age
        self.hungry = hungry
        self.walk = walk

class Dog(Pet):
    species = "Mammal"
    def characteristic(self,breed):
        return "The breed of {} is {} and is a {}".format(self.name, breed, self.species)
    
    def description(self):
        return "{} is {} year(s) old".format(self.name, self.age)

    def is_hungry(self):
        self.hungry = True
    
    def eat(self):
        self.hungry = False
    
    def walking(self):
        self.walk = True


pet1 = Dog("Pooky",8,False,False)
pet2 = Dog("Moana",1,False,False)
pet3 = Dog("Blitzen", 7,False,False)

print("I have 3 dogs")

print(pet1.description())
print(pet1.characteristic("Basset Hound"))
pet1.eat()
if (pet1.walk == True):
    print(pet1.name + " is walking! \n")
elif (pet1.walk == False):
    print(pet1.name + " is not walking! \n")    

print(pet2.description())
print(pet2.characteristic("Chihuahua"))
pet2.eat()
if (pet2.walk == True):
    print(pet2.name + " is walking! \n")
elif (pet2.walk == False):
    print(pet2.name + " is not walking! \n")  

print(pet3.description())
print(pet3.characteristic("Husky"))
pet3.eat
pet3.walking
if (pet3.walk == True):
    print(pet3.name + " is walking! \n")
elif (pet3.walk == False):
    print(pet3.name + " is not walking! \n")  

if (pet1.hungry == True and pet2.hungry == True and pet3.hungry == True):
    print("My dogs are hungry!")
elif(pet1.hungry == False and pet2.hungry == False and pet3.hungry == False):
    print("My dogs are not hungry")