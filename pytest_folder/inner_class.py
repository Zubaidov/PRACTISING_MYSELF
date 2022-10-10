class Student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.laptop = self.Laptop()

    def show(self):
        print(self.name, self.rollno)
        self.laptop.show()

    class Laptop:

        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 16

        def show(self):
            print(self.brand, self.cpu, self.ram)

s1 = Student('Shohruz', 20)
s2 = Student('Shodruz', 18)

s1.show()