class base:
    def __init__(self): 
        self._a=32
        print(self._a)
class derived(base):
    def __init__(self):
        base.__init__(self) # invocking one class inside another one
        print(self._a+2)
class derived1(derived):   #derived1 class is created by derived class 
    def __init__(self):
        derived.__init__(self) #no indentation required because the class inside class 
        print(self._a*2)
    
x=derived1()