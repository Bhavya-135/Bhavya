class father:  # 2 parent classes in this
    fathername=""
    def Father(self):
        print(self.fathername) 

class mother:
    mothername=""
    def Mother(self):
        print(self.mothername)

class son1(father,mother): #with this class we can take entire classes data in this child class
    son1name=""
    def Son1information(self):
        print(self.fathername)
        print(self.mothername)
        print(self.son1name)


s1=son1()                 #objects shoud created only for sons not for parental class
s1.son1name="lava"  
s1.fathername="ram"
s1.mothername="sita"
s1.Son1information()

#example-2

class A:  # 2 parent classes in this
    Aname=""
    def A(self):
        print(self.Aname) 

class B:
    Bname=""
    def B(self):
        print(self.Bname)

class child(A,B): #with this class we can take entire classes data in this child class
    child1name=""
    def child1information(self):
        print(self.Aname)
        print(self.Bname)
        print(self.child1name)
    child2name=""
    def child2information(self):
        print(self.Aname)
        print(self.Bname)
        print(self.child2name)


s1=child()                 #objects shoud created only for sons not for parental class
s1.child1name="lava"  
s1.Aname="ram"
s1.Bname="sita"
s1.child1information()

s2=child()                 #objects shoud created only for sons not for parental class
s2.child2name="lava"  
s2.Aname="ram"
s2.Bname="sita"
s2.child2information()
