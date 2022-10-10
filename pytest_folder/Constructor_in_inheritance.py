class A:
    
    def __init__(self):
        print("In A __init__")

    def feature1(self):
        print("Feature 1 working")
    
    def feature2(self):
        print("Feature 2 working")

class B:

    def __init__(self):
        super().__init__()
        print("In B __init__")

    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")

class C(A, B):

    def __init__(self):
        super().__init__()
        print("In C __init__")

    def feature(self):
        super().feature2()


a1 = C()
a1.feature()
a1.feature4()