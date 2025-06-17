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
print(issubclass(derived,c1))
print(issubclass(derived,c2))
print(issubclass(c2,c1))