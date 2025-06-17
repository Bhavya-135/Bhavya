class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

p1=person("bhavya",20)
print(getattr(p1,"name"))#print(p1.name)
print(getattr(p1,"age"))#print(p1.age)
setattr(p1,"age",21) #21 we can change the value
print(getattr(p1,"age")) 
print(hasattr(p1,"age")) #True  return the boolen value
print(hasattr(p1,"id")) #False