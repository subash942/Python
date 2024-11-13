class Animal:
    def type(self):
        print("This is an animal.")

class Mammal(Animal):
    def fur_type(self):
        print("This mammal has fur.")

class Dog(Mammal):
    def breed(self):
        print("This is a dog.")

class Cat(Mammal):
    def breed(self):
        print("This is a cat.")

class Pet(Dog, Cat):
    pass

p = Pet()

p.type()          
p.fur_type()     
p.breed()        
