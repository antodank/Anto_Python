# Create a new object type called Sample
class Sample:
    pass

# Instance of Sample
x = Sample()

print(type(x))

#Constructor

class Dog:
    
    # Class Object Attribute
    species = 'mammal'
    
    def __init__(self,breed,name):
        self.breed = breed
        self.name = name


dog1 = Dog(breed = 'Lab', name = 'Sam')
dog2 = Dog(breed = 'Huskie', name = 'Moti')
print(f"{dog1.name} is { dog1.breed }")
print(f"{dog2.name} is {dog2.breed}")


#method
class Circle:
    pi = 3.14

    # Circle gets instantiated with a radius (default is 1)
    def __init__(self, radius=1):
        self.radius = radius 
        

    # Method for resetting Radius
    def getArea(self):
        return self.radius * self.radius * self.pi

    # Method for getting Circumference
    def getCircumference(self):
        return self.radius * self.pi * 2

cr1 = Circle()
print(cr1.getArea())
print(cr1.getCircumference())

cr2 = Circle(5)
print(cr2.getArea())
print(cr2.getCircumference())


class Animal:
    def __init__(self):
        print("Animal created")

    def speak(self):
        print("Animal speaking")

    def eat(self):
        print("Animal eating")


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    def speak(self):
        print("Bho - bho")


class Cat(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Cat created")

    def speak(self):
        print("Meaow - Meaow")

""" 
d1 = Dog()
print(d1.speak())

c1 = Cat()
print(c1.speak())
 """
