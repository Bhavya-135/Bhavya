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

class son2(father): 
    son2name=""
    def Son2information(self):
        print(self.fathername)#no mother name is present because only father class we dirived this son2info
        print(self.son2name)

s1=son1()                 #objects shoud created only for sons not for parental class
s1.son1name="lava"  
s1.fathername="ram"
s1.mothername="sita"
s1.Son1information()
s2=son2()      #no mother class here 
s2.fathername="Ram"
s2.son2name="kusha"
s2.Son2information()


"""e-2"""


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

class son2(father): 
    son2name=""
    def Son2information(self):
        print(self.fathername)#no mother name is present because only father class we dirived this son2info
        print(self.son2name)

s1=son1()                 #objects shoud created only for sons not for parental class
s1.son1name="lava"  
s1.fathername="ram"
s1.mothername="sita"
#s1.Son1information()
s2=son2()      #no mother class here 
s2.fathername="Ram"
s2.son2name="kusha"
#s2.Son2information()

s1.mother()
s2.father()