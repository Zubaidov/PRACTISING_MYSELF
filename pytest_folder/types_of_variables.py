#NAMESPACE - is an area where you create and store object/variable

class Cars:

    wheels = 4 #CLASS VARIABLES

    def __init__(self):
        self.mil = 10       #INSTANCE VARIABLES
        self.com = 'BMW'    #INSTANCE VARIABLES


car1 = Cars()
car2 = Cars()

Cars.wheels = 5



print(car1.com, car1.mil, car1.wheels)
print(car2.com, car2.mil, car2.wheels)
