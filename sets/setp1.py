l=input("enter the input values")

A=0
T=0
C=0
G=0
for i in l:
    if i=="A" :
        A+=1
    elif i=="T":
        T+=1
    elif i=="C":
        C+=1
    else:
        G+=1
print("{"+" A :"+str(A)+" T: "+str(T)+" C: "+str(C)+" G :"+str(G)+"}")