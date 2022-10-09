'''class Computer:

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print(f"{self.cpu}, {self.ram},")

com1 = Computer('i5', 16)
com2 = Computer('Ryzen', 8 )

com1.config()
com2.config() 
'''

'''class Computer:
    
    def __init__(self):
        self.name = "hello"
        self.age = 5

    def update(self):
        self.age = 30

c1 = Computer()
c2 = Computer()

c1.name = "C1"
c1.age = 25
c2.name = "C2"
c2.age = 24

c1.update()

print(c1.name, c1.age)
print(c2.name, c2.age)
'''

class Computer:
    def __init__(self):
        self.name = "Hello world"
        self.age = 5

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False
        


c1 = Computer()
c1.name = "C1"
c1.age = 25
c2 = Computer()
c2.name = "C2"
c2.age = 20


if c1.compare(c2):
    print("They are same")
else:
    print("they are different") 

print(c1.name)
print(c2.name)