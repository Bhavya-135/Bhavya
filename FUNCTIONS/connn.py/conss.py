
#without using constrctor
class person:
    name="bhavya"
    age=20
p1=person()
p2=person()
print(p1.name)
print(p2.age)

#without using constrctor
class person:
    name=""
    age=""
p1=person()
p1.name="bhavya"
p1.age="20"
print(p1.name,p1.age)