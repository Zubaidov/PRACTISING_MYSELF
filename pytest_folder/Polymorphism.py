# DUCK TYPING

'''class PyCharm:

    def execute(self):
        print("Compiling")
        print("Running")


class MyEditor:

    def execute(self):
        print("Spell Check")
        print("Convention Check")
        print("Compiling")
        print("Running")


class Laptop:

    def code(self, ide):
        ide.execute()

ide = MyEditor()

lap1 = Laptop()
lap1.code(ide)
'''

#OPERATOR OVERLOADING
'''
a = 5
b = 6
print(a+b)
print(a-b)
print(a*b)
print(int.__add__(a,b)) #MAGIC METHODS
print(int.__sub__(a,b)) #MAGIC METHODS
print(int.__mul__(a,b)) #MAGIC METHODS
'''
class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1,m2)
        return s3

s1 = Student(58, 59)
s2 = Student(60, 65)

s3 = s1 + s2
print(s3.m1)