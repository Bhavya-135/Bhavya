class shape:
    def area(self):
        print("calculate area: ")
class circle(shape):
    def circlearea(self,radius):
        print("area of circle=",3.14*radius*radius)
class square(shape):
    def seqarearea(self,side):
        print("area of square=",side*side)

c1=circle()
c1.area()
c1.circlearea(5)
s1=square()
s1.area()
s1.seqarearea(5)
