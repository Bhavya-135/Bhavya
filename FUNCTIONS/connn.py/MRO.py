class A:
    def myname(self):
        print(" I am in class A")

class B(A):
    def myname(self):
        print(" I am in class B")
class C(A):
    def myname(self):
        print(" I am in class C")


class D(C,B):
    pass
d=D()

print(D.__mro__)
print(D.mro())