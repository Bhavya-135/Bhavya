class Tree:
    def __init__(self,name):
        self.name=name
    def bhavya(self):
        print(self.name)

class mango(Tree):
    def __init__(self, name):
        self.name=name 
    def bhavya1(self):
        print(self.name)
x=Tree(" Trees")
x.bhavya()
y=mango("mango fruits")
y.bhavya1()
y.bhavya()


#example-2
class base:
    def __init__(self): 
        self._a=32
        print(self._a)
class derived(base):
    def __init__(self):
        base.__init__(self) # invocking one class inside another one
        print(self._a+2)
x=base()
y=derived()
print(x._a)  #public data we can use any where  (inheritences proved statement)
print(y._a)  #(inheritences proved statement



#example 3
class bhavya:
    def __init__(self): 
        self._a=0
        print(self._a)
class thirugamalla(bhavya):
    def __init__(self):
        bhavya.__init__(self) # invocking one class inside another one
        print(self._a+135)
x=bhavya()
y=thirugamalla()
print(x._a)  #public data we can use any where  (inheritences proved statement)
print(y._a)  #(inheritences proved statement)
