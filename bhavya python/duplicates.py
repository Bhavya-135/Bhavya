size=int(input("Enter the size of list: "))
u=[1,2,3,4,5,]
list=[]
for i in range(size):
    Temp=int(input(f"Enter the integer value at {i} position"))
    list.append(Temp)
print(f"User entered list : {list}")
for i in list:
    if i not in u:
        u.append(i)
print(f"unique list ",u)