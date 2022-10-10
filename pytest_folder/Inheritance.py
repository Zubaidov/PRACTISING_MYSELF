class A:
    
    def feature1(self):
        print("Feature 1 is working")
    
    def feature2(self):
        print("feature 2 is working")

class B: #NOT INHERIT
    
    def feature3(self):
        print("feature 3 is working")

    def feature4(self):
        print("feature 4 is working")

class C(A): # C INHERIT A

    def feature5(self):
        print("feature 3 is working")

class D(C,B): # MULTIPLE INHERITANCE

    def feature6(self):
        print("feature 3 is working")


a1 = D() # By calling class D you can call all features due to strong inheritance