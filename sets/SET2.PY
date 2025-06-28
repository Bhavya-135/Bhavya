A=list(input("enter the values: "))
k=str(A).split(',')
v=[]
for i in (k):
    if float(i)<=5:
        v.append("Underexpressed")
    elif (float(i)>5 and float(i)<=15):
        v.append("Normal")
    elif float(i)>15:
        v.append("Overexpressed")
print(v)
