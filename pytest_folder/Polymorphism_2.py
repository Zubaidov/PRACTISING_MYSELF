class Dog:
    
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says woof!!!"

class Cat:

    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says meouw!!!"



niko = Dog("Niko")
felix = Cat("Felix")
'''
print(niko.speak())
print(felix.speak())
'''
def pet_speak(pet):
    print(pet.speak())

pet_speak(niko)
pet_speak(felix)
