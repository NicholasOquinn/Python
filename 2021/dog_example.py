def DeepEQTEST(Dog1, Dog2):
    return Dog1.getname() + Dog1.getbreed() + Dog1.getage()\
           == Dog2.getname() + Dog2.getbreed() + Dog2.getage()


class Dog:
    """ A basic representation of a dog.

    attributes: self, name, breed, age
    """
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
    
    def bark(self):
        print("ruff ruff")

    def __str__(self):
        return f"{self.name}, {self.breed}, {self.age}"
        #return self.name + ", " + self.breed + ", " + str(self.age)
    def getname(self):
        return self.name
    def getbreed(self):
        return self.breed
    def getage(self):
        return self.age



rusty = Dog("Rusty", "Beagle", "2")
Toast = Dog("Toast", "Nova Scotia Duck Toller", "4")
Sunny = Dog("Sunny", "Husky/Sheppard", "3")
Sunnie = Dog("Sunny", "Husky/Sheppard", "3")

print(Toast is Sunny)
Marshmallow = Sunny
print(Marshmallow is Sunny)

print(DeepEQTEST(Toast, Sunny))

# Overide __str__ in Dog class to print human-readable object info
print(rusty)

# Using dot notation to call an object method
rusty.bark()

# https://www.python.org/dev/peps/pep-0257/
print(rusty.__doc__)