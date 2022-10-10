class Students:

    school = 'Telusko'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    @classmethod #DECORATOR
    def getschool(cls):
        return cls.school

    @staticmethod
    def info():
        print("This is Student class.. in abc module")

s1 = Students(34,67,32)
s2 = Students(15,32,12)

print(s1.avg())
print(Students.getschool())
Students.info()
