class person:
    # with constructor 
    def __init__(self,name,age):
        self.name=name 
        self.age=age 

    #nornmal printing
    def printing(self):
        print(self.name,self.age)


    #decide 
    def decide(self):
        if self.age > 18:
            print("Major")
        else:
            print("minor")
    # upper
    def uppercase(self):
        k=self.name.upper()
        print(k)
    #length
    def length(self):
        m=self.name
        l=len(m)
        print(l)
        p=self.name
        print(len(p))

p1=person("Bhavya",20)
p2=person("nitya",22)
p1.printing()
p2.printing()
p1.decide()
p2.decide()
p1.uppercase()
p2.uppercase()
p1.length()
p2.length()