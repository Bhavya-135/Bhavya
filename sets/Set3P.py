first_name=input("enter the value")
secound_name=input("enter the value")
v=[]
l=0

k=len(first_name)
m=len(secound_name)
#Not same length
if k!=m:
    print("Error")
if k==m:
    for i in range(k):
        if first_name[i]==secound_name[i]:
            l+=1
        elif first_name[i]!=secound_name[i]:
            v.append(i)
print(v)