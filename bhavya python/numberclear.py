size=int(input("Enter the number"))
list=[]
for i in range(size):
    value=int(input(f"enter the value at {i} Index:"))
    list.append(value)
for i in range (size):
   if(list[i]<0):
       list[i]=0
for i in range(size):
   if(list[i]%3==0):
       print(list[i])