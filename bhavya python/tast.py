size=int(input("Enter the length list"))
list=[]
for i in range(size):
        Temp=input(f"Enter the integer value at {i} position")
        list.append(Temp)
print("songs in normal order")
print(list)
print(f"unique list ",u)
print(list[::-1])