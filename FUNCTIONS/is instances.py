class c1:
    def sum(self,a,b):
        return a+b;
class c2:
    def mult(self,a,b):
        return a*b;
class derived(c1,c2):
    def div(self,a,b):
        return a/b;
d=derived()
print(isinstance(d,c1))
print(isinstance(d,c2))
print(isinstance(d,c1))