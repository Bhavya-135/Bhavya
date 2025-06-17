size=int(input("Enter the number"))
k=[]
for i in range (size):
    Temp=int(input(f"Enter the interger value{i}:"))
    k.append(Temp)
print(k[::-1])
print("user enter list",k)