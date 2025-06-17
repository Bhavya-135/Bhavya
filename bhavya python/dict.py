Jobrole={101:"Front-end Developer",102:"Back-end developer",103:"sf"}
print(Jobrole)
print(type(Jobrole))
print(Jobrole[101])
print(Jobrole[102])
print(Jobrole[103])


Jobrole[101]='UI/UX Developer'
print(Jobrole)

Jobrole[104]="Data Engineer"
print(Jobrole)  

Jobrole[105]="python developer"
print(Jobrole)

Jobrole[106]="Data analyst"
print(Jobrole)

#deliting
Jobrole.pop(101)
print(Jobrole)
del Jobrole[104]
print(Jobrole)

#len
print(len(Jobrole))

print(Jobrole.keys())
print(Jobrole.values())
print(Jobrole.items())
#update

b={4:"four"}
Jobrole.update(b)
print(Jobrole)
#fromkeys
key={"apple","ball"}
value="for kids"
print(Jobrole.fromkeys(key,value))